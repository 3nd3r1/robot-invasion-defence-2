""" src/ui/lose_menu.py """
import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup

from utils.config import fonts, colors
from utils.file_reader import get_font
from utils.text import draw_text


class LoseMenu:
    """ Static class for the lose game menu """
    menu_buttons = MenuButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        LoseMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    @staticmethod
    def load_menu(screen, restart_game, quit_game):
        restart_pos = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 50)
        quit_pos = (restart_pos[0], restart_pos[1] + 100)

        LoseMenu.menu_buttons.add(MenuButton("try again", restart_pos, restart_game))
        LoseMenu.menu_buttons.add(MenuButton("back to main menu", quit_pos, quit_game))

    @staticmethod
    def draw(screen):
        font = LoseMenu.fonts["default"]
        color = colors["default_font_color"]
        draw_text(screen, font, color, "YOU LOST", (screen.get_width() / 2 + 50, 180))
        LoseMenu.menu_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        LoseMenu.menu_buttons.on_click(pos)
