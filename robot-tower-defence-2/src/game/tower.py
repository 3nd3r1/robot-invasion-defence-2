from abc import ABC, abstractmethod
import pygame

from utils.math import get_angle
from utils.logger import logger
from utils.config import colors


class Tower(pygame.sprite.Sprite, ABC):
    """
      This class represents a tower that can be placed on the map.
      It has properties such as cost, range, and damage,
      and methods for upgrading and selling the tower. 
    """

    def __init__(self, game):
        super().__init__()
        self.image = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.__game = game
        self.__placing = True
        self.__target = None

        self.__last_shot = 0

    def place(self, pos) -> bool:
        """ Place the tower on the map """
        if not self.__placing:
            return False

        self.rect.center = pos
        if self.is_valid_position():
            self.__placing = False
            self.get_game().add_tower(self)
            logger.debug(f"Placing tower at {pos}")
            return True

        return False

    def draw(self, screen):
        """ Blits the tower to the screen """
        if self.__placing:
            range_color = colors["valid_tower_range"]
            if not self.is_valid_position():
                range_color = colors["invalid_tower_range"]

            range_circle = pygame.Surface(
                (self.get_range()*2, self.get_range()*2), pygame.constants.SRCALPHA, 32)
            pygame.draw.circle(range_circle, range_color,
                               (self.get_range(), self.get_range()), self.get_range())
            screen.blit(range_circle, (self.rect.centerx-self.get_range(),
                        self.rect.centery-self.get_range()))

        screen.blit(self.image, self.rect)

    def update(self):
        self._draw_tower()

        if self.__placing:
            self.rect.center = pygame.mouse.get_pos()
            return

        self.__target = self.get_game().get_closest_robot_in_range(self)
        now = pygame.time.get_ticks()

        if self.get_target() and now - self.__last_shot >= self.get_shoot_interval():
            self.__last_shot = now
            self._shoot()

    def on_click(self):
        """ This is called when the tower is clicked """
        return

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """
        if not self.get_target():
            return 0

        difference_x = self.get_target().rect.centerx - self.rect.centerx
        difference_y = self.get_target().rect.centery - self.rect.centery
        return get_angle(difference_x, difference_y)+90

    def get_target(self):
        """ Returns the target """
        return self.__target

    def get_game(self):
        """ Returns the game """
        return self.__game

    def get_last_shot(self):
        """ Returns the time of the last shot """
        return self.__last_shot

    def is_valid_position(self) -> bool:
        """ Returns true if the tower is a valid position """
        for tower in self.get_game().get_towers():
            if tower.get_hitbox().colliderect(self.get_hitbox()):
                return False

        if self.get_game().get_map().is_in_obstacle(self.get_hitbox()):
            return False

        if self.get_game().get_map().is_in_path(self.get_hitbox()):
            return False

        if self.get_game().get_map().is_in_water(self.get_hitbox()) and not self.can_be_in_water():
            return False

        if not self.get_game().get_map().is_in_map(self.get_hitbox()):
            return False

        return True

    @staticmethod
    @abstractmethod
    def load_images() -> None:
        pass

    @staticmethod
    @abstractmethod
    def render_tower(angle: float) -> pygame.Surface:
        pass

    @abstractmethod
    def _draw_tower(self) -> None:
        pass

    @abstractmethod
    def _shoot(self) -> None:
        pass

    @abstractmethod
    def get_range(self) -> int:
        pass

    @abstractmethod
    def get_hitbox(self) -> pygame.Rect:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass

    @abstractmethod
    def get_shoot_interval(self) -> int:
        pass

    @abstractmethod
    def can_be_in_water(self) -> bool:
        pass
