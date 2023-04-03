""" src/game/ui.py """
import pygame
from game.ui_components.tower_button import TowerButton
from utils.file_reader import get_image
from utils.images import GAME_BACKGROUND


class Ui:
    """
      This class represents the user interface of the game.
      It has methods for displaying information about the game, such as the player's score and the number of lives remaining. 
    """

    def __init__(self) -> None:
        self.__image = pygame.image.load(get_image(GAME_BACKGROUND))
        self.__tower_buttons = pygame.sprite.Group()

    def draw(self, surface) -> None:
        """ Draws all components to the screen """
        surface.blit(self.__image, (0, 0))

    def __draw_tower_buttons(self) -> None:
        self.__tower_buttons.add(TowerButton(""))
