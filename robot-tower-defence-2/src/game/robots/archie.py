import pygame

from game.robot import Robot
from utils.config import robots, images


class Archie(Robot):
    """ ARCHIE - Advanced Robust Combat Heavy Intelligent Exterminator """

    def __init__(self, game) -> None:
        health = robots["archie"]["health"]
        self.speed = robots["archie"]["speed"]
        self.__base_damage = robots["archie"]["base_damage"]
        self.__base_bounty = robots["archie"]["base_bounty"]

        self.__animation_interval = robots["archie"]["animation_interval"]
        self.__path_offset = pygame.math.Vector2(
            robots["archie"]["path_offset"])
        self.__sheet_size = images["robots"]["archie"]["walk_sheet_size"]

        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "archie"

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
