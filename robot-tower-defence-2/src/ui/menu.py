import pygame

from ui.menus import StartGameMenu, MainMenu

from game.game import Game

from utils.logger import logger
from utils.config import general


class Menu:
    fonts = {}

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((general["screen_width"], general["screen_height"]))
        self.__running = True

        self.__state = "main_menu"

        self.__load_assets()
        self.__load_menus()

    def __load_assets(self):
        MainMenu.load_assets()
        StartGameMenu.load_assets()

    def __load_menus(self):
        MainMenu.load_menu(self.__screen, self.set_state, self.quit_game)
        StartGameMenu.load_menu(self.__screen, self.start_game)

    def draw(self):

        screen = self.__screen
        screen.fill((0, 0, 0))

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

    def quit_game(self):
        self.__running = False

    def set_state(self, state):
        self.__state = state