""" src/game/projectile.py """
import math
import pygame

from abc import ABC, abstractmethod

from utils.math import get_angle


class Projectile(pygame.sprite.Sprite, ABC):
    """ Projectile class """

    def __init__(self, tower, target, starting_pos, start_offset):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()

        self.__target = target
        self.__tower = tower
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

        velocity_x = min(math.cos(alph)*self.get_speed(), abs(
            self.rect.centerx - self.get_target().rect.centerx))
        velocity_y = min(math.sin(alph)*self.get_speed(), abs(
            self.rect.centery - self.get_target().rect.centery))
        self.__velocity = (velocity_x, velocity_y)

        self.rect.move_ip(self.__velocity)
        self._draw_projectile()

        if self.get_target().rect.collidepoint(self.rect.center):
            self._target_hit()
            self.get_target().lose_health(self.get_damage())
            self.kill()

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """
        if not self.get_target():
            return 90

        difference_x = self.get_target().rect.centerx - self.rect.centerx
        difference_y = self.get_target().rect.centery - self.rect.centery
        return get_angle(difference_x, difference_y)+90

    def get_target(self):
        """ Returns the target """
        return self.__target

    def get_tower(self):
        """ Returns the tower """
        return self.__tower

    @abstractmethod
    def _target_hit(self) -> None:
        pass

    @abstractmethod
    def _draw_projectile(self) -> None:
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def get_damage(self) -> int:
        pass
