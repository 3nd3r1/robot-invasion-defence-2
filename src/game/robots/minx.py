""" src/game/robots/minx.py """
import pygame
from game.robot import Robot
from utils.config import robots, images


class Minx(Robot):
    """ MINX - Miniature Infiltrating Nimble Exterminator"""

    def __init__(self, game) -> None:
        health = robots["minx"]["health"]
        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "minx"

    @property
    def speed(self) -> int:
        return robots["minx"]["speed"]

    @property
    def damage(self) -> int:
        return robots["minx"]["base_damage"] + self.health

    @property
    def bounty(self) -> int:
        return robots["minx"]["base_bounty"]

    @property
    def _animation_interval(self) -> int:
        return robots["minx"]["animation_interval"]

    @property
    def _path_offset(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(robots["minx"]["path_offset"])

    @property
    def _sheet_size(self) -> tuple:
        return images["robots"]["minx"]["walk_sheet_size"]
