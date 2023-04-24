import pygame

from ui.components.tower_button import TowerButton

from utils.config import colors, images, fonts
from utils.file_reader import get_image, get_font


class GameUi:
    images = {}
    fonts = {}

    def __init__(self, game):
        self.__game = game
        self.__tower_buttons = pygame.sprite.Group()
        self.__load_tower_buttons()

    @staticmethod
    def load_assets():
        GameUi.images["background"] = pygame.image.load(get_image(images["ui"]["game_background"]))
        GameUi.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 60)
        TowerButton.load_assets()

    def __load_tower_buttons(self):
        self.__tower_buttons.add(TowerButton("turret", (65, 150)))
        self.__tower_buttons.add(TowerButton("missile_launcher", (65, 265)))
        self.__tower_buttons.add(TowerButton("cannon", (65, 375)))

    def draw(self, screen):
        game = self.__game

        # Draw background
        screen.blit(GameUi.images["background"], (0, 0))

        # Draw towers
        self.__tower_buttons.draw(screen)

        # Draw game info
        self.__draw_text(screen, f"HP {game.get_player().get_health()}", (200, 20))
        self.__draw_text(screen, f"${game.get_player().get_money()}", (320, 20))

        round_num = game.get_round_manager().get_round()
        max_round = game.get_round_manager().get_rounds_amount()
        self.__draw_text(screen, f"ROUND: {round_num}/{max_round}", (850, 20))

    def on_click(self, pos):
        """ Checks if a tower button was clicked """
        game = self.__game

        for button in self.__tower_buttons:
            if button.rect.collidepoint(pos):
                button.on_click()
                game.create_tower(button.tower_name)

    def __draw_text(self, screen, text, pos):
        font = GameUi.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        screen.blit(text, pos)
