""" src/game/towers/turret.py """
import pygame
from game.tower import Tower
from game.projectile import Projectile
from utils.config import towers
from utils.file_reader import get_image
from utils.math import get_angle
from utils.logger import logger


class Turret(Tower):
    """ Turret tower class """

    def __init__(self, game: "Game") -> None:
        super().__init__()
        self._game = game

        self._range = towers["turret"]["range"]
        self._can_be_in_water = towers["turret"]["can_be_in_water"]
        self._shoot_interval = towers["turret"]["shoot_interval"]
        self._hitbox = pygame.Rect(0, 0, 100, 100)

        self.__load_images()

    def __load_images(self) -> None:
        self._images = []
        base = pygame.image.load(get_image(towers["base"]))
        model_1 = pygame.image.load(get_image(towers["turret"]["model_1"]))
        model_2 = pygame.image.load(get_image(towers["turret"]["model_2"]))
        model_3 = pygame.image.load(get_image(towers["turret"]["model_3"]))

        base = pygame.transform.scale_by(base, 0.25)
        model_1 = pygame.transform.scale_by(model_1, 0.40)
        model_2 = pygame.transform.scale_by(model_2, 0.40)
        model_3 = pygame.transform.scale_by(model_3, 0.40)

        self._images.append(base)
        self._images.append(model_1)
        self._images.append(model_2)
        self._images.append(model_3)

    def _shoot(self) -> None:
        """ Shoots a turret projectile """
        if not self._target:
            return
        self._game.add_projectile(
            TurretProjectile(self._target, self.rect.center))


class TurretProjectile(Projectile):
    def __init__(self, target: "Robot", starting_pos) -> None:
        super().__init__(starting_pos)
        self._target = target
        self._speed = towers["turret"]["projectile_speed"]
        self._damage = towers["turret"]["projectile_damage"]

        self.__render_projectile()

    def __render_projectile(self) -> None:

        projectile = pygame.image.load(
            get_image(towers["turret"]["projectile"]))
        projectile = pygame.transform.scale_by(projectile, 0.75)

        dx = self._target.rect.centerx - self.rect.centerx
        dy = self._target.rect.centery - self.rect.centery

        projectile_offset = pygame.math.Vector2(
            towers["turret"]["projectile_start_offset"])
        projectile_offset = projectile_offset.rotate(get_angle(dx, dy))

        self.image = pygame.Surface((50, 50), pygame.constants.SRCALPHA, 32)
        self.image.blit(projectile, (0, 0))
        self.image = pygame.transform.rotate(self.image, -get_angle(dx, dy))

        self.rect = self.image.get_rect(
            center=self.rect.center).move(projectile_offset)
