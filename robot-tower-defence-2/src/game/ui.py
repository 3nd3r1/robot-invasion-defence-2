""" src/game/ui.py """
import pygame
from game.ui_components.tower_button import TowerButton
from utils.file_reader import get_image
from utils.config import images


class Ui:
    """
      This class represents the user interface of the game.
      It has methods for displaying information about the game,
      such as the player's score and the number of lives remaining. 
    """

    def __init__(self, game):
        self.__image = pygame.image.load(get_image(images["game_background"]))
        self.__tower_buttons = pygame.sprite.Group()
        self.__game = game

        self.__load_tower_buttons()

    def draw(self, surface):
        """ Draws all components to the screen """
        surface.blit(self.__image, (0, 0))
        self.__tower_buttons.draw(surface)

    def on_click(self, pos):
        """ Checks if a tower button was clicked """
        for button in self.__tower_buttons:
            if button.rect.collidepoint(pos):
                button.on_click()
                self.__game.create_tower(button.tower_name)

    def __load_tower_buttons(self):
        self.__tower_buttons.add(TowerButton("turret", (70, 166)))
        self.__tower_buttons.add(TowerButton("missile_launcher", (70, 285)))
        self.__tower_buttons.add(TowerButton("cannon", (70, 405)))
