import pygame

from game.robot import Robot
from utils.config import robots, images


class Archie(Robot):
    """ ARCHIE - Advanced Robust Combat Heavy Intelligent Exterminator """

    def __init__(self, game) -> None:
        health = robots["archie"]["health"]
        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "archie"

    @property
    def speed(self) -> int:
        return robots["archie"]["speed"]

    @property
    def damage(self) -> int:
        return robots["archie"]["base_damage"] + self.health

    @property
    def bounty(self) -> int:
        return robots["archie"]["base_bounty"]

    @property
    def _animation_interval(self) -> int:
        return robots["archie"]["animation_interval"]

    @property
    def _path_offset(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(robots["archie"]["path_offset"])

    @property
    def _sheet_size(self) -> tuple:
        return images["robots"]["archie"]["walk_sheet_size"]
