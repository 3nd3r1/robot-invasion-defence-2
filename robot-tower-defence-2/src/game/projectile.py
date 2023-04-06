""" src/game/projectile.py """
import pygame
import math


class Projectile(pygame.sprite.Sprite):
    """ Projectile class """

    def __init__(self, starting_pos) -> None:
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = starting_pos

        self._speed = 1
        self._velocity = (0, 0)

        self._target = None

    def update(self) -> None:
        """ Updates the projectile """
        if not self._target or not self._target.alive():
            self.kill()
            return

        if self._target.rect.centerx-self.rect.centerx == 0:
            alph = math.pi/2
        else:
            alph = math.atan(abs(self._target.rect.centery-self.rect.centery) /
                             abs(self._target.rect.centerx-self.rect.centerx))
            if self._target.rect.centery-self.rect.centery < 0:
                alph = -alph
            if self._target.rect.centerx - self.rect.centerx < 0:
                alph = math.pi - alph

        self._velocity = (min(math.cos(alph)*self._speed, abs(
            self.rect.centerx - self._target.rect.centerx)), min(math.sin(alph)*self._speed, abs(
                self.rect.centery - self._target.rect.centery)))

        self.rect.move_ip(self._velocity)

        if self._target.rect.collidepoint(self.rect.center):
            self._target.lose_health(self._damage)
            self.kill()
