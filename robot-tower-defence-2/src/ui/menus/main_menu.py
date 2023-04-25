""" src/ui/main_menu.py """
import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup
from utils.config import colors, fonts
from utils.file_reader import get_font


class MainMenu:
    """ Static class for the main menu """
    buttons = MenuButtonGroup()
    fonts = {}

    @staticmethod
    def load_assets():
        MainMenu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    @staticmethod
    def load_menu(screen, set_state, quit_game):
        start_pos = (screen.get_width() / 2 + 50, screen.get_height() / 2 - 50)
        quit_pos = (start_pos[0], start_pos[1] + 100)

        MainMenu.buttons.add(MenuButton("Start Game", start_pos, set_state, "start_game_menu"))
        MainMenu.buttons.add(MenuButton("Quit", quit_pos, quit_game))

    @staticmethod
    def draw(screen):
        title_pos = (screen.get_width()/2+50, 180)

        MainMenu.draw_text(screen, "Robot Invasion Defence II", title_pos)
        MainMenu.buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        MainMenu.buttons.on_click(pos)

    @staticmethod
    def draw_text(screen, text, pos):
        font = MainMenu.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)
