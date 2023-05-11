""" src/game/projectile.py """
from abc import ABC, abstractmethod
import math
import pygame

from utils.math import get_angle
from utils.config import images
from utils.file_reader import get_image


class ProjectileGroup(pygame.sprite.Group):
    def draw(self, screen):
        for projectile in self.sprites():
            projectile.draw(screen)


class Projectile(pygame.sprite.Sprite, ABC):
    """ Projectile class """
    images = {}

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

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_Projectile__g"] = {}
        state["image"] = None
        return state

    @staticmethod
    def load_assets():
        """ Loads the assets """
        Projectile.load_projectile_assets("turret")
        Projectile.load_projectile_assets("missile_launcher")
        Projectile.load_projectile_assets("cannon")

    @staticmethod
    def load_projectile_assets(tower_type):
        """ Loads assets for a specific towers projectile """
        projectile = pygame.image.load(get_image(images["projectiles"][tower_type][0]))
        projectile = pygame.transform.scale_by(projectile, images["projectiles"][tower_type][1])
        Projectile.images[tower_type] = projectile

    @staticmethod
    def render(tower_type, target_angle):
        """ Renders the projectile """
        screen = pygame.Surface((50, 50), pygame.constants.SRCALPHA, 32)

        projectile = Projectile.images[tower_type]
        projectile = pygame.transform.rotate(projectile, -target_angle)

        projectile_rect = projectile.get_rect(center=screen.get_rect().center)
        screen.blit(projectile, projectile_rect)

        return screen

    def draw(self, screen):
        """ Draws the projectile """
        self.image = Projectile.render(self.tower.type, self.get_target_angle())
        screen.blit(self.image, self.rect)

    def update(self):
        """ Updates the projectile """
        if not self.target or not self.target.alive():
            self.kill()
            return

        self.__calculate_velocity()

        self.rect.move_ip(self.__velocity)

        if self.target.rect.collidepoint(self.rect.center):
            self._target_hit()
            self.target.lose_health(self.damage)
            self.kill()

    def __calculate_velocity(self):
        if self.target.rect.centerx-self.rect.centerx == 0:
            alph = math.pi/2
        else:
            alph = math.atan(abs(self.target.rect.centery-self.rect.centery) /
                             abs(self.target.rect.centerx-self.rect.centerx))
            if self.target.rect.centery-self.rect.centery < 0:
                alph = -alph
            if self.target.rect.centerx - self.rect.centerx < 0:
                alph = math.pi - alph

        velocity_x = min(math.cos(alph)*self.speed, abs(
            self.rect.centerx - self.target.rect.centerx))
        velocity_y = min(math.sin(alph)*self.speed, abs(
            self.rect.centery - self.target.rect.centery))

        self.__velocity = (velocity_x, velocity_y)

    def get_target_angle(self) -> float:
        """ Returns the angle to the target """
        if not self.target:
            return 90

        difference_x = self.target.rect.centerx - self.rect.centerx
        difference_y = self.target.rect.centery - self.rect.centery
        return get_angle(difference_x, difference_y)+90

    @property
    def target(self):
        """ Returns the target """
        return self.__target

    @property
    def tower(self):
        """ Returns the tower """
        return self.__tower

    @abstractmethod
    def _target_hit(self) -> None:
        """ Called when the target is hit """""

    @property
    @abstractmethod
    def speed(self) -> float:
        pass

    @property
    @abstractmethod
    def damage(self) -> int:
        pass
