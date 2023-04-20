""" src/game/ui.py """
import pygame
from game.ui_components.tower_button import TowerButton
from utils.file_reader import get_image, get_font
from utils.config import images, fonts, colors


class Ui:
    """
      This class represents the user interface of the game.
      It has methods for displaying information about the game,
      such as the player's score and the number of lives remaining. 
    """
    images = {}
    fonts = {}

    def __init__(self, game):
        self.__tower_buttons = pygame.sprite.Group()
        self.__game = game

        self.__load_tower_buttons()

    @staticmethod
    def load_assets():
        """ Loads all assets """
        Ui.images["background"] = pygame.image.load(get_image(images["ui"]["game_background"]))
        Ui.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 60)

    def draw(self, screen):
        """ Draws all components to the screen """
        background_image = Ui.images["background"]

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw tower buttons
        self.__tower_buttons.draw(screen)

        # Draws texts
        self.__draw_text(screen, f"HP {self.__game.get_player().get_health()}", (200, 20))
        self.__draw_text(screen, f"${self.__game.get_player().get_money()}", (320, 20))
        self.__draw_text(screen, f"ROUND: {self.__game.get_round_manager().get_round()}", (850, 20))

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

    def __draw_text(self, screen, text, pos):
        font = Ui.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        screen.blit(text, pos)
