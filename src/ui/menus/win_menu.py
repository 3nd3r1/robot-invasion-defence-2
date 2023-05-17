""" src/ui/win_menu.py """
import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup

from utils.config import fonts, colors
from utils.file_reader import get_font
from utils.text import draw_text


class WinMenu:
    """ Static class for the win game menu """
    menu_buttons = MenuButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        WinMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    @staticmethod
    def load_menu(screen, quit_game):
        quit_pos = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 50)

        WinMenu.menu_buttons.add(MenuButton("back to main menu", quit_pos, quit_game))

    @staticmethod
    def draw(screen):
        font = WinMenu.fonts["default"]
        color = colors["default_font_color"]
        draw_text(screen, font, color, "YOU WON", (screen.get_width() / 2 + 50, 180))
        WinMenu.menu_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        WinMenu.menu_buttons.on_click(pos)
