""" src/game/ui_components/tower_button.py """
import pygame
from game.towers import Turret, MissileLauncher, Cannon
from utils.config import fonts, colors, towers, images
from utils.file_reader import get_font, get_image


class TowerButton(pygame.sprite.Sprite):
    """ Tower button class """
    fonts = {}
    images = {}

    def __init__(self, tower, pos):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=pos).move(7, 0)

        self.tower_name = tower
        self.__cost = towers[tower]["cost"]

        self.__render_icon()
        self.__render_price()

    @staticmethod
    def load_assets():
        TowerButton.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 30)
        TowerButton.images["background"] = pygame.image.load(
            get_image(images["ui"]["tower_button_background"]))

    def __render_icon(self):
        """ Render the towers icon """
        if self.tower_name == "turret":
            icon_image = Turret.render_tower(90)
        elif self.tower_name == "missile_launcher":
            icon_image = MissileLauncher.render_tower(90)
        elif self.tower_name == "cannon":
            icon_image = Cannon.render_tower(90)

        icon_image = pygame.transform.scale_by(icon_image, 0.90)
        icon_rect = icon_image.get_rect(center=(35, 40))

        self.image = TowerButton.images["background"].copy()
        self.image.blit(icon_image, icon_rect)

    def __render_price(self):
        """ Render the towers name and price"""
        self.__draw_text(self.image, f"${self.__cost}", (45, 77))

    def __draw_text(self, screen, text, pos):
        font = TowerButton.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)

    def on_click(self):
        return
