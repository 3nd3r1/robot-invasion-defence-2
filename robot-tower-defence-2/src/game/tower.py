import pygame
from utils.logger import logger
from utils.math import get_angle


class Tower(pygame.sprite.Sprite):
    """ This class represents a tower that can be placed on the map. It has properties such as cost, range, and damage, and methods for upgrading and selling the tower. """

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self._game = None

        self.__placing = True
        self._target = None

        self.__shoot_timer = 0

    def place(self) -> None:
        """ Place the tower on the map """
        self.__placing = False

    def _render_tower(self) -> None:
        """ Renders the tower can be overwritten by child class"""
        self.image = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        base = self._images[0]
        model_1 = self._images[1]

        tower_offset = pygame.math.Vector2(-10, -15)

        if self._target:
            dx = self._target.rect.centerx - self.rect.centerx
            dy = self._target.rect.centery - self.rect.centery
            model_1 = pygame.transform.rotate(
                model_1, -get_angle(dx, dy))
            tower_offset = tower_offset.rotate(get_angle(dx, dy))

        base_rect = base.get_rect(
            center=self.image.get_rect().center)
        tower_rect = model_1.get_rect(
            center=base_rect.center).move(tower_offset)

        self.image.blit(base, base_rect)
        self.image.blit(model_1, tower_rect)

    def draw(self, screen) -> None:
        """ Draws the tower to the screen """
        if self.__placing:
            pygame.draw.circle(screen, (50, 50, 50), self.rect.center,
                               self._range,  1)
        screen.blit(self.image, self.rect)

    def update(self) -> None:
        self._render_tower()
        if self.__placing:
            self.rect.center = pygame.mouse.get_pos()
            return

        self._target = self._game.get_closest_robot_in_range(self)
        if self._target and self.__shoot_timer >= self._shoot_interval:
            self.__shoot_timer = 0
            self._shoot()

        self.__shoot_timer += 1

    def on_click(self) -> None:
        """ This is called when the tower is clicked """
        pass

    def can_be_in_water(self) -> bool:
        """ Returns if the tower can be placed in water """
        return self._can_be_in_water

    def get_range(self) -> int:
        """ Returns the range of the tower """
        return self._range

    def get_hitbox(self) -> pygame.Rect:
        """ Returns the hitbox of the tower """
        self._hitbox.center = self.rect.center
        return self._hitbox
