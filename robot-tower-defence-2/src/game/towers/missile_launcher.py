""" src/game/towers/missile_launcher.py """
import pygame

from game.tower import Tower
from game.projectile import Projectile
from game.particle import Particle

from utils.config import towers
from utils.math import distance_between_points


class MissileLauncher(Tower):
    """ Missile Launcher tower class """

    def _animate_tower(self):
        """ Draws the tower to the sprite image """
        target_angle = self.get_target_angle()
        time_now = pygame.time.get_ticks()

        if time_now-self.last_shot >= self.shoot_interval:
            projectile_image = Projectile.render("missile_launcher", target_angle)
            projectile_rect = projectile_image.get_rect(center=self.image.get_rect().center)
            projectile_rect.move_ip(pygame.math.Vector2(0, -30).rotate(target_angle))
            self.image.blit(projectile_image, projectile_rect)

    def _shoot(self):
        self.game.sprites.projectiles.add(
            MissileLauncherProjectile(self, self.target, self.rect.center))

    @property
    def type(self) -> str:
        return "missile_launcher"

    @property
    def can_be_in_water(self) -> bool:
        """ Returns if the tower can be in water """
        return towers["missile_launcher"]["can_be_in_water"]

    @property
    def range(self) -> int:
        """ Returns the range of the tower """
        return towers["missile_launcher"]["range"]

    @property
    def shoot_interval(self) -> int:
        return towers["missile_launcher"]["shoot_interval"]

    @property
    def hitbox(self):
        hitbox = pygame.Rect(0, 0, 60, 60)
        hitbox.center = self.rect.center
        return hitbox

    @property
    def cost(self) -> int:
        return towers["missile_launcher"]["cost"]


class MissileLauncherProjectile(Projectile):
    images = {}

    def __init__(self, tower, target, starting_pos) -> None:
        self.__speed = towers["missile_launcher"]["projectile_speed"]
        self.__damage = towers["missile_launcher"]["projectile_damage"]
        self.__explosion_radius = towers["missile_launcher"]["projectile_explosion_radius"]
        self.__explosion_damage = towers["missile_launcher"]["projectile_explosion_damage"]

        start_offset = towers["missile_launcher"]["projectile_start_offset"]

        super().__init__(tower, target, starting_pos, start_offset)

    def _target_hit(self):
        if not self.target.rect.collidepoint(self.rect.center):
            return

        explosion = Particle("explosion", self.target.rect.center)
        self.tower.game.sprites.particles.add(explosion)

        for robot in self.tower.game.sprites.robots:
            distance = distance_between_points(robot.rect.center, self.rect.center)
            if distance <= self.__explosion_radius:
                robot.lose_health(self.__explosion_damage)

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def damage(self) -> int:
        return self.__damage
