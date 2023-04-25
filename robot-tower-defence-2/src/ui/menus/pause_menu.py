""" src/ui/start_game_menu.py """
import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup
from ui.components.icon_button import IconButton, IconButtonGroup

from utils.config import fonts, colors, images
from utils.file_reader import get_font


class PauseMenu:
    """ Static class for the start game menu """
    menu_buttons = MenuButtonGroup()
    icon_buttons = IconButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        PauseMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    @staticmethod
    def load_menu(screen, unpause_game):
        continue_pos = (67, 100)
        restart_pos = (screen.get_width() / 2, screen.get_height() / 2 - 100)
        PauseMenu.icon_buttons.add(IconButton(
            images["ui"]["continue_button"], continue_pos, unpause_game))
        PauseMenu.menu_buttons.add(MenuButton("restart", restart_pos, unpause_game))

    @staticmethod
    def draw(screen):
        PauseMenu.draw_text(screen, "Pause Game", (screen.get_width() / 2, 100))
        PauseMenu.menu_buttons.draw(screen)
        PauseMenu.icon_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        PauseMenu.menu_buttons.on_click(pos)
        PauseMenu.icon_buttons.on_click(pos)

    @staticmethod
    def draw_text(screen, text, pos):
        font = PauseMenu.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)
