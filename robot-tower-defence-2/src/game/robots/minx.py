""" src/game/robots/minx.py """
import pygame
from game.robot import Robot
from utils.config import robots, images
from utils.sheet_reader import get_sheet_images


class Minx(Robot):
    """ MINX - Miniature Infiltrating Nimble Exterminator"""
    images = {}

    def __init__(self, game) -> None:
        health = robots["minx"]["health"]
        self.__speed = robots["minx"]["speed"]
        self.__base_damage = robots["minx"]["base_damage"]
        self.__base_bounty = robots["minx"]["base_bounty"]
        self.__path_offset = pygame.math.Vector2(robots["minx"]["path_offset"])

        self.__animation_frame = 0
        self.__last_animation = 0
        self.__animation_interval = robots["minx"]["animation_interval"]

        super().__init__(game, health)

    @staticmethod
    def load_images():
        sheet_image = images["robots"]["minx"]["walk_sheet"]
        sheet_size = images["robots"]["minx"]["walk_sheet_size"]

        Minx.images["walking"] = get_sheet_images(sheet_image, sheet_size)

    @staticmethod
    def render_robot(frame: int) -> pygame.Surface:
        return Minx.images["walking"][frame].copy()

    def _draw_robot(self) -> None:

        velocity = self.get_velocity()
        tile_width = images["robots"]["minx"]["walk_sheet_size"][0]
        offset = 0

        if velocity[0] < 0 and velocity[1] == 0:
            offset = tile_width*1
        elif velocity[0] > 0 and velocity[1] == 0:
            offset = tile_width*3
        elif velocity[0] == 0 and velocity[1] < 0:
            offset = tile_width*0
        else:
            offset = tile_width*2

        now = pygame.time.get_ticks()
        if now-self.__last_animation >= self.__animation_interval:
            self.__animation_frame = ((
                self.__animation_frame + 1) % tile_width) + offset
            self.__last_animation = now

        self.image = Minx.render_robot(self.__animation_frame)

    def get_bounty(self) -> int:
        return self.__base_bounty

    def get_damage(self) -> int:
        return self.__base_damage + self.get_health()

    def get_speed(self) -> int:
        return self.__speed

    def get_path_offset(self) -> pygame.math.Vector2:
        return self.__path_offset
