import pygame

from ui.components.menu_button import MenuButton, MenuButtonGroup

from game.game import Game

from utils.logger import logger
from utils.file_reader import get_font
from utils.config import general, fonts, colors


class Menu:
    fonts = {}

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((general["screen_width"], general["screen_height"]))
        self.__running = True

        self.__load_assets()
        self.__load_main_menu()

    def __load_assets(self):
        Menu.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 100)
        MenuButton.load_assets()

    def __load_main_menu(self):
        self.__main_menu = MenuButtonGroup()

        start_pos = (self.__screen.get_width() / 2, self.__screen.get_height() / 2 - 100)
        quit_pos = (start_pos[0], start_pos[1] + 100)

        self.__main_menu.add(MenuButton("Start Game", start_pos, self.start_game, "grass_fields"))
        self.__main_menu.add(MenuButton("Quit", quit_pos, self.quit_game))

    def draw(self):
        self.__screen.fill((0, 0, 0))
        self.__draw_text("Robot Invasion Defence II", (self.__screen.get_width() / 2, 100))
        self.__main_menu.draw(self.__screen)
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
        self.__main_menu.on_click(pos)
        logger.debug(f"Clicked on {pos} with {button}")

    def __draw_text(self, text, pos):
        font = Menu.fonts["default"]
        font_color = colors["default_font_color"]
        text_img = font.render(text, True, font_color)
        text_rect = text_img.get_rect(center=pos)

        self.__screen.blit(text_img, text_rect)

    def start_game(self, arena="grass_fields"):
        game = Game(arena)
        game.run()

    def quit_game(self):
        self.__running = False
