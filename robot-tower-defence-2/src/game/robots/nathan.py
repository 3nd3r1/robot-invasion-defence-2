import pygame

from game.robot import Robot

from utils.config import robots, images
from utils.sheet_reader import get_sheet_images


class Nathan(Robot):
    """ NATHAN - Neural Autonomous Tactical Hunter Assassin Networked """
    images = {}

    def __init__(self, game) -> None:
        health = robots["nathan"]["health"]
        self.__speed = robots["nathan"]["speed"]
        self.__base_damage = robots["nathan"]["base_damage"]
        self.__base_bounty = robots["nathan"]["base_bounty"]
        self.__path_offset = pygame.math.Vector2(
            robots["nathan"]["path_offset"])

        self.__animation_frame = 0
        self.__animation_timer = 0
        self.__animation_interval = robots["nathan"]["animation_interval"]

        super().__init__(game, health)

    @staticmethod
    def load_images():
        sheet_image = images["robots"]["nathan"]["walk_sheet"]
        sheet_size = images["robots"]["nathan"]["walk_sheet_size"]

        Nathan.images["walking"] = get_sheet_images(sheet_image, sheet_size)

    @staticmethod
    def render_robot(frame: int) -> pygame.Surface:
        return Nathan.images["walking"][frame].copy()

    def _draw_robot(self) -> None:

        velocity = self.get_velocity()
        offset = 0

        if velocity[0] < 0 and velocity[1] == 0:
            offset = 8
        elif velocity[0] > 0 and velocity[1] == 0:
            offset = 24
        elif velocity[0] == 0 and velocity[1] < 0:
            offset = 0
        else:
            offset = 16

        if self.__animation_timer >= self.__animation_interval:
            self.__animation_frame = ((
                self.__animation_frame + 1) % 8) + offset
            self.__animation_timer = 0
        self.__animation_timer += 1

        self.image = Nathan.render_robot(self.__animation_frame)

    def get_speed(self) -> int:
        return self.__speed

    def get_damage(self) -> int:
        return self.__base_damage

    def get_bounty(self) -> int:
        return self.__base_bounty + self.get_health()

    def get_path_offset(self) -> pygame.math.Vector2:
        return self.__path_offset
