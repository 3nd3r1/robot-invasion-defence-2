""" src/ui/start_game_menu.py """
import pygame

from ui.components.start_game_button import StartGameButtonGroup, StartGameButton

from utils.config import fonts, colors
from utils.file_reader import get_font


class StartGameMenu:
    """ Static class for the start game menu """
    buttons = StartGameButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        StartGameMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        StartGameButton.load_assets()

    @staticmethod
    def load_menu(screen, start_game):
        start_pos = (screen.get_width() / 2, screen.get_height() / 2 - 100)

        StartGameMenu.buttons.add(StartGameButton(
            "Grass Fields", start_pos, start_game, "grass_fields"))

    @staticmethod
    def draw(screen):
        StartGameMenu.draw_text(screen, "Select Arena", (screen.get_width() / 2, 100))
        StartGameMenu.buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        StartGameMenu.buttons.on_click(pos)

    @staticmethod
    def draw_text(screen, text, pos):
        font = StartGameMenu.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)
