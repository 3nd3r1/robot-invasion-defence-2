import pygame

from game.robot import Robot

from utils.config import robots, images


class Nathan(Robot):
    """ NATHAN - Neural Autonomous Tactical Hunter Assassin Networked """

    def __init__(self, game) -> None:
        health = robots["nathan"]["health"]
        super().__init__(game, health)

    @property
    def type(self) -> str:
        return "nathan"

    @property
    def speed(self) -> int:
        return robots["nathan"]["speed"]

    @property
    def damage(self) -> int:
        return robots["nathan"]["base_damage"] + self.health

    @property
    def bounty(self) -> int:
        return robots["nathan"]["base_bounty"]

    @property
    def _animation_interval(self) -> int:
        return robots["nathan"]["animation_interval"]

    @property
    def _path_offset(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(robots["nathan"]["path_offset"])

    @property
    def _sheet_size(self) -> tuple:
        return images["robots"]["nathan"]["walk_sheet_size"]
