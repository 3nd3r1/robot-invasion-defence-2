import pygame

from game.robot import Robot

from utils.config import robots, images


class Nathan(Robot):
    """ NATHAN - Neural Autonomous Tactical Hunter Assassin Networked """

    def __init__(self, game) -> None:
        health = robots["nathan"]["health"]
        self.__speed = robots["nathan"]["speed"]
        self.__base_damage = robots["nathan"]["base_damage"]
        self.__base_bounty = robots["nathan"]["base_bounty"]

        self.__path_offset = pygame.math.Vector2(
            robots["nathan"]["path_offset"])
        self.__sheet_size = images["robots"]["nathan"]["walk_sheet_size"]
        self.__animation_interval = robots["nathan"]["animation_interval"]

        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "nathan"

    @property
    def speed(self) -> int:
        return self.__speed

    @property
    def damage(self) -> int:
        return self.__base_damage + self.health

    @property
    def bounty(self) -> int:
        return self.__base_bounty

    @property
    def _animation_interval(self) -> int:
        return self.__animation_interval

    @property
    def _path_offset(self) -> pygame.math.Vector2:
        return self.__path_offset

    @property
    def _sheet_size(self) -> tuple:
        return self.__sheet_size
