""" src/ui/pause_menu.py """
import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup
from ui.components.icon_button import IconButton, IconButtonGroup

from utils.config import fonts, colors, images
from utils.file_reader import get_font
from utils.text import draw_text


class PauseMenu:
    """ Static class for the pause game menu """
    menu_buttons = MenuButtonGroup()
    icon_buttons = IconButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        PauseMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    @staticmethod
    def load_menu(screen, unpause_game, restart_game, quit_game):
        continue_pos = (67, 100)
        restart_pos = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 50)
        quit_pos = (restart_pos[0], restart_pos[1] + 100)

        PauseMenu.icon_buttons.add(IconButton(
            images["ui"]["back_button"], continue_pos, unpause_game))

        PauseMenu.menu_buttons.add(MenuButton("restart", restart_pos, restart_game))
        PauseMenu.menu_buttons.add(MenuButton("back to main menu", quit_pos, quit_game))

    @staticmethod
    def draw(screen):
        font = PauseMenu.fonts["default"]
        color = colors["default_font_color"]
        draw_text(screen, font, color, "Game Paused", (screen.get_width() / 2 + 50, 180))
        PauseMenu.menu_buttons.draw(screen)
        PauseMenu.icon_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        PauseMenu.menu_buttons.on_click(pos)
        PauseMenu.icon_buttons.on_click(pos)
