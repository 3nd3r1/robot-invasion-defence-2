""" src/ui/start_game_menu.py """
import pygame

from ui.components.start_game_button import StartGameButtonGroup, StartGameButton
from ui.components.icon_button import IconButtonGroup, IconButton

from utils.config import fonts, colors, images
from utils.file_reader import get_font


class StartGameMenu:
    """ Static class for the start game menu """
    select_buttons = StartGameButtonGroup()
    icon_buttons = IconButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        StartGameMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        StartGameButton.load_assets()

    @staticmethod
    def load_menu(screen, set_state, start_game):
        start_pos = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 50)

        StartGameMenu.select_buttons.add(StartGameButton(
            "Grass Fields", start_pos, start_game, "grass_fields"))

        StartGameMenu.icon_buttons.add(IconButton(
            images["ui"]["back_button"], (67, 100), set_state, "main_menu"))

    @staticmethod
    def draw(screen):
        title_pos = (screen.get_width() / 2 + 50, 180)
        StartGameMenu.draw_text(screen, "Select Arena", title_pos)
        StartGameMenu.select_buttons.draw(screen)
        StartGameMenu.icon_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        StartGameMenu.select_buttons.on_click(pos)
        StartGameMenu.icon_buttons.on_click(pos)

    @staticmethod
    def draw_text(screen, text, pos):
        font = StartGameMenu.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)
