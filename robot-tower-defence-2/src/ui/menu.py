import pygame

from ui.menus import StartGameMenu, MainMenu

from game.game import Game

from utils.logger import logger
from utils.file_reader import get_image, get_font
from utils.config import general, images, colors, fonts
from utils.db import get_player_info
from utils.text import draw_text


class Menu:
    fonts = {}
    images = {}

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(
            (general["screen_width"], general["screen_height"]))

        pygame.display.set_caption("Robot Tower Defence 2")
        icon = pygame.image.load(get_image(images["ui"]["icon"]))
        pygame.display.set_icon(icon)

        self.__running = True
        self.__state = "main_menu"

        self.__player_info = get_player_info()

        self.__load_assets()
        self.__load_menus()

    def __load_assets(self):

        # Load fonts
        Menu.fonts["player_info"] = pygame.font.Font(
            get_font(fonts["default"]), 50)

        # Load images
        Menu.images["background"] = pygame.image.load(
            get_image(images["ui"]["ui_background"]))

        # Load menu assets
        MainMenu.load_assets()
        StartGameMenu.load_assets()

    def __load_menus(self):
        MainMenu.load_menu(self.__screen, self.set_state, self.quit_game)
        StartGameMenu.load_menu(self.__screen, self.set_state, self.start_game)

    def draw(self):
        """ Draws the menu that corresponds to the current state"""

        screen = self.__screen

        # Draw background
        screen.fill(colors["menu_background"])
        screen.blit(Menu.images["background"], (0, 0))

        # Draw player info
        info_font = Menu.fonts["player_info"]
        font_color = colors["default_font_color"]

        player_info = self.__player_info

        draw_text(screen, info_font, font_color, f"Money: {player_info['coins']}", (250, 50))
        draw_text(screen, info_font, font_color, f"XP: {player_info['experience']}", (1000, 50))

        # Draw menu
        if self.__state == "main_menu":
            MainMenu.draw(screen)
        elif self.__state == "start_game_menu":
            StartGameMenu.draw(screen)

        pygame.display.flip()

    def run(self):
        while self.__running:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    self.__running = False
                elif evt.type == pygame.constants.MOUSEBUTTONDOWN:
                    self.__on_click(evt.pos, evt.button)
            self.draw()

    def __on_click(self, pos, button):
        if self.__state == "main_menu":
            MainMenu.on_click(pos)
        elif self.__state == "start_game_menu":
            StartGameMenu.on_click(pos)

        logger.debug(f"Clicked on {pos} with {button}")

    def start_game(self, arena="grass_fields"):
        game = Game(arena)
        game.run()
        self.__player_info = get_player_info()
        self.__load_menus()

    def quit_game(self):
        self.__running = False

    def set_state(self, state):
        self.__state = state
