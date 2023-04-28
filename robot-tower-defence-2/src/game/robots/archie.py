import pygame

from game.robot import Robot
from utils.sheet_reader import get_sheet_images
from utils.config import robots, images


class Archie(Robot):
    """ ARCHIE - Advanced Robust Combat Heavy Intelligent Exterminator """
    images = {}

    def __init__(self, game) -> None:
        health = robots["archie"]["health"]
        self.__speed = robots["archie"]["speed"]
        self.__base_damage = robots["archie"]["base_damage"]
        self.__base_bounty = robots["archie"]["base_bounty"]
        self.__path_offset = pygame.math.Vector2(
            robots["archie"]["path_offset"])

        self.__animation_frame = 0
        self.__animation_timer = 0
        self.__animation_interval = robots["archie"]["animation_interval"]

        super().__init__(game, health)

    @staticmethod
    def load_images():
        sheet_image = images["robots"]["archie"]["walk_sheet"]
        sheet_size = images["robots"]["archie"]["walk_sheet_size"]
        Archie.images["walking"] = get_sheet_images(sheet_image, sheet_size)

    @staticmethod
    def render_robot(frame: int) -> pygame.Surface:
        return Archie.images["walking"][frame].copy()

    def draw(self) -> None:
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

        self.image = Archie.render_robot(self.__animation_frame)

    def get_bounty(self) -> int:
        return self.__base_bounty

    def get_damage(self) -> int:
        return self.__base_damage + self.get_health()

    def get_speed(self) -> int:
        return self.__speed

    def get_path_offset(self) -> pygame.math.Vector2:
        return self.__path_offset
