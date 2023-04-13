import pygame

from abc import ABC, abstractmethod

from utils.logger import logger
from utils.math import get_angle


class Tower(pygame.sprite.Sprite, ABC):
    """ This class represents a tower that can be placed on the map. It has properties such as cost, range, and damage, and methods for upgrading and selling the tower. """

    def __init__(self, game: "Game") -> None:
        super().__init__()
        self.image = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.__game = game
        self.__placing = True
        self.__target = None

        self.__last_shot = 0

    def place(self) -> None:
        """ Place the tower on the map """
        self.__placing = False

    def draw(self, screen) -> None:
        """ Blits the tower to the screen """
        if self.__placing:
            pygame.draw.circle(screen, (50, 50, 50), self.rect.center,
                               self.get_range(),  1)
        screen.blit(self.image, self.rect)

    def update(self) -> None:
        self._draw_tower()

        if self.__placing:
            self.rect.center = pygame.mouse.get_pos()
            return

        self.__target = self.get_game().get_closest_robot_in_range(self)
        now = pygame.time.get_ticks()

        if self.get_target() and now - self.__last_shot >= self.get_shoot_interval():
            self.__last_shot = now
            self._shoot()

    def on_click(self) -> None:
        """ This is called when the tower is clicked """
        pass

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """
        if not self.get_target():
            return 0

        dx = self.get_target().rect.centerx - self.rect.centerx
        dy = self.get_target().rect.centery - self.rect.centery
        return get_angle(dx, dy)+90

    def get_target(self) -> "Robot":
        """ Returns the target """
        return self.__target

    def get_game(self) -> "Game":
        """ Returns the game """
        return self.__game

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
    def can_be_in_water(self) -> bool:
        pass

    @abstractmethod
    def get_shoot_interval(self) -> int:
        pass
