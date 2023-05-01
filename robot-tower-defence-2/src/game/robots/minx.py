""" src/game/robots/minx.py """
import pygame
from game.robot import Robot
from utils.config import robots, images


class Minx(Robot):
    """ MINX - Miniature Infiltrating Nimble Exterminator"""

    def __init__(self, game) -> None:
        health = robots["minx"]["health"]
        self.__speed = robots["minx"]["speed"]
        self.__base_damage = robots["minx"]["base_damage"]
        self.__base_bounty = robots["minx"]["base_bounty"]

        self.__path_offset = pygame.math.Vector2(robots["minx"]["path_offset"])
        self.__sheet_size = images["robots"]["minx"]["walk_sheet_size"]
        self.__animation_interval = robots["minx"]["animation_interval"]

        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "minx"

    @property
    def bounty(self) -> int:
        return self.__base_bounty

    @property
    def damage(self) -> int:
        return self.__base_damage + self.health

    @property
    def speed(self) -> int:
        return self.__speed

    @property
    def _animation_interval(self) -> int:
        return self.__animation_interval

    @property
    def _path_offset(self) -> pygame.math.Vector2:
        return self.__path_offset

    @property
    def _sheet_size(self) -> tuple:
        return self.__sheet_size
