""" src/game/projectile.py """
import math
import pygame

from abc import ABC, abstractmethod

from utils.math import get_angle


class Projectile(pygame.sprite.Sprite, ABC):
    """ Projectile class """

    def __init__(self, target: "Robot", starting_pos: tuple, start_offset: tuple) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.__target = target
        self.__velocity = (0, 0)

        self.rect.center = starting_pos
        self.rect.move_ip(pygame.math.Vector2(
            start_offset).rotate(self.get_target_angle()))

    def update(self) -> None:
        """ Updates the projectile """
        if not self.get_target() or not self.get_target().alive():
            self.kill()
            return

        if self.get_target().rect.centerx-self.rect.centerx == 0:
            alph = math.pi/2
        else:
            alph = math.atan(abs(self.get_target().rect.centery-self.rect.centery) /
                             abs(self.get_target().rect.centerx-self.rect.centerx))
            if self.get_target().rect.centery-self.rect.centery < 0:
                alph = -alph
            if self.get_target().rect.centerx - self.rect.centerx < 0:
                alph = math.pi - alph

        self.__velocity = (min(math.cos(alph)*self.get_speed(), abs(
            self.rect.centerx - self.get_target().rect.centerx)), min(math.sin(alph)*self.get_speed(), abs(
                self.rect.centery - self.get_target().rect.centery)))

        self.rect.move_ip(self.__velocity)
        self._draw_projectile()

        if self.get_target().rect.collidepoint(self.rect.center):
            self.get_target().lose_health(self.get_damage())
            self.kill()

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """
        if not self.get_target():
            return 90

        dx = self.get_target().rect.centerx - self.rect.centerx
        dy = self.get_target().rect.centery - self.rect.centery
        return get_angle(dx, dy)+90

    def get_target(self) -> "Robot":
        """ Returns the target """
        return self.__target

    @abstractmethod
    def _draw_projectile(self) -> None:
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def get_damage(self) -> int:
        pass
