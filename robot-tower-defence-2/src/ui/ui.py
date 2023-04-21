""" src/game/ui.py """
import pygame

from ui.game_ui import GameUi
from utils.file_reader import get_image, get_font
from utils.config import images, fonts, colors, general


class Ui:
    """
      This class represents the user interface.
      It has methods for displaying information about the game,
      such as the player's score and the number of lives remaining. 
    """
    images = {}
    fonts = {}

    def __init__(self):
        flags = 0

        self.__screen = pygame.display.set_mode(
            (general["display_width"], general["display_height"]), flags)
        self.__game = None
        self.__game_ui = GameUi(self)

    @staticmethod
    def load_assets():
        """ Loads all assets """
        Ui.images["background"] = pygame.image.load(get_image(images["ui"]["game_background"]))
        Ui.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 60)
        GameUi.load_assets()

    def draw(self):
        """ Draws all components to the screen """
        background_image = Ui.images["background"]
        screen = self.__screen

        # Draw background
        screen.blit(background_image, (0, 0))

        self.__game_ui.draw(screen)
