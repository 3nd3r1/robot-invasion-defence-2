import os
import __main__
import pygame
from utils.IMAGES import GAME_BACKGROUND


class Hud:
    def __init__(self) -> None:
        pass

    def draw(self, surface) -> None:
        main_dir = os.path.dirname(__main__.__file__)
        game_background_file = os.path.join(main_dir, GAME_BACKGROUND)
        image = pygame.image.load(game_background_file)
        surface.blit(GAME_BACKGROUND, (0, 0))
