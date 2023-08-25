""" src/ui/game_ui.py """
import pygame

from ui.components.tower_button import TowerButton, TowerButtonGroup
from ui.components.icon_button import IconButton, IconButtonGroup
from ui.menus import PauseMenu, LoseMenu, WinMenu

from utils.config import colors, images, fonts
from utils.file_reader import get_image, get_font
from utils.text import draw_text


class GameUi:
    images = {}
    fonts = {}

    def __init__(self, game):
        self.__game = game
        self.__screen = pygame.display.get_surface()

        self.__tower_buttons = TowerButtonGroup(game.create_tower)
        self.__icon_buttons = IconButtonGroup()

        self.__load_tower_buttons()
        self.__load_icon_buttons()
        self.__load_menus()

    @staticmethod
    def load_assets():
        GameUi.images["background"] = pygame.image.load(get_image(images["ui"]["ui_background"]))
        GameUi.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 60)
        TowerButton.load_assets()
        PauseMenu.load_assets()
        LoseMenu.load_assets()
        WinMenu.load_assets()

    def __load_tower_buttons(self):
        self.__tower_buttons.add(TowerButton("turret", (65, 150)))
        self.__tower_buttons.add(TowerButton("missile_launcher", (65, 265)))
        self.__tower_buttons.add(TowerButton("cannon", (65, 375)))

    def __load_icon_buttons(self):
        self.__icon_buttons.add(IconButton(
            images["ui"]["pause_button"], (67, 500), self.__game.pause_game))

    def __load_menus(self):
        PauseMenu.load_menu(self.__screen, self.__game.unpause_game,
                            self.__game.restart_game, self.__game.kill)
        LoseMenu.load_menu(self.__screen, self.__game.restart_game, self.__game.kill)
        WinMenu.load_menu(self.__screen, self.__game.kill)

    def draw(self, screen):
        game = self.__game
        state = game.state.state

        # Draw background
        if state != "game":
            screen.fill(colors["menu_background"])
        screen.blit(GameUi.images["background"], (0, 0))

        if state == "game":
            # Draw tower buttons
            self.__tower_buttons.draw(screen, game.player.money)

            # Draw icon buttons
            self.__icon_buttons.draw(screen)

            # Draw game info
            font = GameUi.fonts["default"]
            color = colors["default_font_color"]
            draw_text(screen, font, color, f"HP {game.player.health}", (250, 50))
            draw_text(screen, font, color, f"${game.player.money}", (400, 50))

            round_num = game.round_manager.round
            max_round = game.round_manager.rounds_amount
            draw_text(screen, font, color, f"ROUND: {round_num}/{max_round}", (950, 50))
        elif state == "pause":
            PauseMenu.draw(screen)
        elif state == "lose":
            LoseMenu.draw(screen)
        elif state == "win":
            WinMenu.draw(screen)

    def on_click(self, pos):
        """ Checks if a tower button was clicked """
        game = self.__game
        state = game.state.state

        if state == "game":
            self.__tower_buttons.on_click(pos, game.player.money)
            self.__icon_buttons.on_click(pos)
        elif state == "pause":
            PauseMenu.on_click(pos)
        elif state == "lose":
            LoseMenu.on_click(pos)
        elif state == "win":
            WinMenu.on_click(pos)
