""" src/game/towers/turret.py """
import pygame

from game.tower import Tower
from game.projectile import Projectile

from utils.config import towers
from utils.file_reader import get_image
from utils.logger import logger


class Turret(Tower):
    """ Turret tower class """

    images = {}

    def __init__(self, game: "Game") -> None:
        self.__can_be_in_water = towers["turret"]["can_be_in_water"]
        self.__range = towers["turret"]["range"]
        self.__shoot_interval = towers["turret"]["shoot_interval"]
        self.__hitbox = pygame.Rect(0, 0, 100, 100)

        super().__init__(game)

    @staticmethod
    def load_images() -> None:
        base = pygame.image.load(get_image(towers["base"]))
        model_1 = pygame.image.load(get_image(towers["turret"]["model_1"]))
        model_2 = pygame.image.load(get_image(towers["turret"]["model_2"]))
        model_3 = pygame.image.load(get_image(towers["turret"]["model_3"]))

        base = pygame.transform.scale_by(base, 0.25)
        model_1 = pygame.transform.scale_by(model_1, 0.40)
        model_2 = pygame.transform.scale_by(model_2, 0.40)
        model_3 = pygame.transform.scale_by(model_3, 0.40)

        Turret.images["base"] = base
        Turret.images["model_1"] = model_1
        Turret.images["model_2"] = model_2
        Turret.images["model_3"] = model_3

        TurretProjectile.load_images()

    @staticmethod
    def render_tower(angle: float) -> pygame.Surface:
        """ Renders the tower """
        screen = pygame.Surface((150, 150), pygame.constants.SRCALPHA, 32)
        base = Turret.images["base"]
        model_1 = Turret.images["model_1"]

        tower_offset = pygame.math.Vector2(-10, -15)

        model_1 = pygame.transform.rotate(model_1, -angle)
        tower_offset = tower_offset.rotate(angle)

        base_rect = base.get_rect(center=screen.get_rect().center)
        tower_rect = model_1.get_rect(
            center=base_rect.center).move(tower_offset)

        screen.blit(base, base_rect)
        screen.blit(model_1, tower_rect)
        return screen

    def _draw_tower(self) -> None:
        """ Draws the tower to the sprite image """
        self.image = Turret.render_tower(self.get_target_angle())

    def _shoot(self) -> None:
        """ Shoots a turret projectile """
        if not self.get_target():
            return
        self.get_game().add_projectile(
            TurretProjectile(self.get_target(), self.rect.center))

    def can_be_in_water(self) -> bool:
        """ Returns if the tower can be in water """
        return self.__can_be_in_water

    def get_range(self) -> int:
        """ Returns the range of the tower """
        return self.__range

    def get_shoot_interval(self) -> int:
        return self.__shoot_interval

    def get_hitbox(self) -> pygame.Rect:
        return self.__hitbox


class TurretProjectile(Projectile):
    images = {}

    def __init__(self, target: "Robot", starting_pos) -> None:
        self.__speed = towers["turret"]["projectile_speed"]
        self.__damage = towers["turret"]["projectile_damage"]

        start_offset = towers["turret"]["projectile_start_offset"]

        super().__init__(target, starting_pos, start_offset)

    @staticmethod
    def load_images() -> None:
        projectile = pygame.image.load(
            get_image(towers["turret"]["projectile"]))
        projectile = pygame.transform.scale_by(projectile, 0.75)
        TurretProjectile.images["projectile"] = projectile

    @staticmethod
    def render_projectile(angle: float) -> pygame.Surface:
        """ Renders the projectile """
        screen = pygame.Surface((50, 50), pygame.constants.SRCALPHA, 32)

        projectile = TurretProjectile.images["projectile"]
        projectile = pygame.transform.rotate(projectile, -angle)

        projectile_rect = projectile.get_rect(
            center=screen.get_rect().center)

        screen.blit(projectile, projectile_rect)
        return screen

    def _draw_projectile(self) -> None:
        self.image = TurretProjectile.render_projectile(
            self.get_target_angle())

    def get_speed(self) -> float:
        return self.__speed

    def get_damage(self) -> int:
        return self.__damage
