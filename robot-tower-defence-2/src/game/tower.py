from abc import ABC, abstractmethod
import pygame

from utils.math import get_angle
from utils.logger import logger
from utils.config import colors, images
from utils.file_reader import get_image


class TowerGroup(pygame.sprite.Group):
    def draw(self, screen):
        for tower in self.sprites():
            tower.draw(screen)

    def on_click(self, pos):
        """ This is called when the tower is clicked """
        for tower in self.sprites():
            if tower.rect.collidepoint(pos):
                tower.on_click()
            else:
                tower.on_unclick()


class Tower(pygame.sprite.Sprite, ABC):
    """
      This class represents a tower that can be placed on the map.
      It has properties such as cost, range, and damage,
      and methods for upgrading and selling the tower. 

        Attributes:
            cost (int): The cost of the tower.
            range (int): The range of the tower.
            damage (int): The amount of damage the tower does to the robot.
            target (Robot): The robot the tower is targeting.
            type (str): The type of the tower.
            shoot_interval (int): The amount of time between shots.
            hitbox (pygame.Rect): The hitbox of the tower.
    """

    images = {}

    def __init__(self, game):
        super().__init__()
        self.image = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.__game = game
        self.__state = "placing"  # placing, idle, clicked

        self.__target = None
        self.__target_angle = 0
        self.__last_shot = 0

        self.__model = "model_1"

    @staticmethod
    def load_assets():
        """ Load the assets for the tower """
        base = pygame.image.load(get_image(images["towers"]["base"][0]))
        base = pygame.transform.scale_by(base, images["towers"]["base"][1])

        Tower.images["base"] = base
        Tower.load_tower_assets("cannon")
        Tower.load_tower_assets("missile_launcher")
        Tower.load_tower_assets("turret")

    @staticmethod
    def load_tower_assets(tower):
        model_1 = pygame.image.load(get_image(images["towers"][tower]["model_1"][0]))
        model_2 = pygame.image.load(get_image(images["towers"][tower]["model_2"][0]))
        model_3 = pygame.image.load(get_image(images["towers"][tower]["model_3"][0]))

        model_1 = pygame.transform.scale_by(model_1, images["towers"][tower]["model_1"][1])
        model_2 = pygame.transform.scale_by(model_2, images["towers"][tower]["model_2"][1])
        model_3 = pygame.transform.scale_by(model_3, images["towers"][tower]["model_3"][1])

        Tower.images[tower] = {}
        Tower.images[tower]["model_1"] = model_1
        Tower.images[tower]["model_2"] = model_2
        Tower.images[tower]["model_3"] = model_3

    @staticmethod
    def render(tower, model, angle):
        """ Renders the tower """
        surface = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        base = Tower.images["base"]
        tower_image = Tower.images[tower][model]
        tower_image = pygame.transform.rotate(tower_image, -angle)

        tower_offset = pygame.math.Vector2(images["towers"][tower][model][2]).rotate(angle)

        base_rect = base.get_rect(center=surface.get_rect().center)
        tower_rect = tower_image.get_rect(center=base_rect.center).move(tower_offset)

        surface.blit(base, base_rect)
        surface.blit(tower_image, tower_rect)
        return surface

    def place(self, pos) -> bool:
        """ Place the tower on the map """
        if self.__state != "placing":
            return False

        self.rect.center = pos
        if self.is_valid_position():
            self.__state = "idle"
            self.game.sprites.towers.add(self)
            logger.debug(f"Placing tower at {pos}")
            return True

        return False

    def draw(self, screen):
        """ Blits the tower to the screen """
        if self.__state in ("placing", "clicked"):
            self.__draw_range_circle(screen)

        self.image = Tower.render(self.type, self.model, self.get_target_angle())
        self._animate_tower()
        screen.blit(self.image, self.rect)

    def __draw_range_circle(self, screen):
        """ Draws the range circle """
        range_color = colors["valid_tower_range"]
        if not self.is_valid_position():
            range_color = colors["invalid_tower_range"]

        range_circle = pygame.Surface((self.range*2, self.range*2), pygame.constants.SRCALPHA, 32)
        pygame.draw.circle(range_circle, range_color, (self.range, self.range), self.range)
        screen.blit(range_circle, (self.rect.centerx-self.range, self.rect.centery-self.range))

    def update(self):
        if self.__state == "placing":
            self.rect.center = pygame.mouse.get_pos()
            return

        self.__target = self.game.get_closest_robot_in_range(self)
        now = pygame.time.get_ticks()

        if self.target and now - self.last_shot >= self.shoot_interval:
            self.__last_shot = now
            self._shoot()

    def on_click(self):
        """ This is called when the tower is clicked """
        self.__state = "clicked"

    def on_unclick(self):
        """ This is called when the tower is unclicked """
        self.__state = "idle"

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """

        if self.target:
            difference_x = self.target.rect.centerx - self.rect.centerx
            difference_y = self.target.rect.centery - self.rect.centery
            self.__target_angle = get_angle(difference_x, difference_y)+90

        return self.__target_angle

    def is_valid_position(self) -> bool:
        """ Returns true if the tower is a valid position """
        for tower in self.game.sprites.towers:
            if tower.hitbox.colliderect(self.hitbox):
                return False

        if self.game.map.is_in_obstacle(self.hitbox):
            return False

        if self.game.map.is_in_path(self.hitbox):
            return False

        if self.game.map.is_in_water(self.hitbox) and not self.can_be_in_water:
            return False

        if not self.game.map.is_in_map(self.hitbox):
            return False

        return True

    @property
    def target(self):
        """ Returns the target """
        return self.__target

    @property
    def last_shot(self):
        """ Returns the time of the last shot """
        return self.__last_shot

    @property
    def model(self):
        """ Returns the model """
        return self.__model

    @property
    def game(self):
        """ Returns the game """
        return self.__game

    @abstractmethod
    def _animate_tower(self) -> None:
        """ Animates the tower """

    @abstractmethod
    def _shoot(self) -> None:
        """ Shoots a projectile """

    @property
    @abstractmethod
    def type(self) -> str:
        """ Returns the type of the tower """

    @property
    @abstractmethod
    def range(self) -> int:
        """ Returns the range of the tower """

    @property
    @abstractmethod
    def hitbox(self) -> pygame.Rect:
        """ Returns the hitbox of the tower """

    @property
    @abstractmethod
    def cost(self) -> int:
        """ Returns the cost of the tower """

    @property
    @abstractmethod
    def shoot_interval(self) -> int:
        """ Returns the shoot interval of the tower"""

    @property
    @abstractmethod
    def can_be_in_water(self) -> bool:
        """ Returns true if the tower can be placed in water """
