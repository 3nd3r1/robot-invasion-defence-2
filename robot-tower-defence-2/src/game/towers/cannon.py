""" src/game/towers/cannon.py """
import pygame

from game.tower import Tower
from game.projectile import Projectile

from utils.config import towers


class Cannon(Tower):
    """ Cannon tower class """

    def _shoot(self):
        self.game.sprites.projectiles.add(CannonProjectile(self, self.target, self.rect.center))

    def _animate_tower(self):
        return

    @property
    def type(self) -> str:
        return "cannon"

    @property
    def can_be_in_water(self) -> bool:
        """ Returns if the tower can be in water """
        return towers["cannon"]["can_be_in_water"]

    @property
    def range(self) -> int:
        """ Returns the range of the tower """
        return towers["cannon"]["range"]

    @property
    def shoot_interval(self) -> int:
        return towers["cannon"]["shoot_interval"]

    @property
    def hitbox(self):
        hitbox = pygame.Rect(0, 0, 60, 60)
        hitbox.center = self.rect.center
        return hitbox

    @property
    def cost(self) -> int:
        return towers["cannon"]["cost"]


class CannonProjectile(Projectile):
    def __init__(self, tower, target, starting_pos) -> None:
        self.__speed = towers["cannon"]["projectile_speed"]
        self.__damage = towers["cannon"]["projectile_damage"]

        start_offset = towers["cannon"]["projectile_start_offset"]

        super().__init__(tower, target, starting_pos, start_offset)

    def _target_hit(self):
        return

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def damage(self) -> int:
        return self.__damage
