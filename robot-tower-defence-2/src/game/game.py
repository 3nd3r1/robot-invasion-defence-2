""" Main game file """
import pygame
import pygame.constants
from utils.round_generator import generate_rounds
from utils.logger import logger
from utils import SETTINGS
from game.map.map import Map
from game.ui.ui import Ui


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena: str) -> None:
        self.__loading = True
        self.__paused = False
        self.__screen = pygame.display.set_mode(
            (SETTINGS.DISPLAY_WIDTH, SETTINGS.DISPLAY_HEIGHT))
        self.__round = 1
        self.__arena = arena

        self.__ui = Ui()
        self.__map = Map(arena)

        self.__towers = pygame.sprite.Group()
        self.__robots = pygame.sprite.Group()
        self.__rounds = []

        self.__initialize_rounds()
        self.__loading = False

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__arena)
        logger.debug("Rounds initialized.")

    def next_round(self) -> None:
        self.__round += 1

    def update(self) -> None:
        self.__towers.update()
        self.__robots.update()

    def draw(self, screen) -> None:
        self.__map.draw(screen)
        self.__ui.draw(screen)
        self.__towers.draw(screen)
        self.__robots.draw(screen)

    def run(self) -> None:
        while not self.__paused:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    return
            self.update()
            self.draw(self.__screen)
            pygame.display.flip()
