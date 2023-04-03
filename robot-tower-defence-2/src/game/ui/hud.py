import os
import __main__
import pygame
from utils.IMAGES import GAME_BACKGROUND
from utils.file_reader import get_image


class Hud:
    def __init__(self) -> None:
        self.__image = pygame.image.load(get_image(GAME_BACKGROUND))
        self.__image = pygame.transform.scale(self.__image, (960, 640))

    def draw(self, surface) -> None:
        surface.blit(self.__image, (0, 0))
