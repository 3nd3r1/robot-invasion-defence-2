""" src/game/ui_components/tower_button.py """
import pygame
from game.tower import Tower
from utils.config import fonts, colors, towers, images
from utils.file_reader import get_font, get_image


class TowerButtonGroup(pygame.sprite.Group):
    def __init__(self, create_tower):
        super().__init__()
        self.__create_tower = create_tower

    def draw(self, screen, player_money):
        for sprite in self.sprites():
            affordable = player_money >= sprite.cost
            sprite.render_price(affordable)
            screen.blit(sprite.image, sprite.rect)

    def on_click(self, pos, player_money):
        for sprite in self.sprites():
            if sprite.rect.collidepoint(pos):
                if player_money >= sprite.cost:
                    self.__create_tower(sprite.tower_name)


class TowerButton(pygame.sprite.Sprite):
    """ Tower button class """
    fonts = {}
    images = {}

    def __init__(self, tower, pos):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=pos).move(7, 0)

        self.tower_name = tower
        self.cost = towers[tower]["cost"]

        self.__render_icon()

    @staticmethod
    def load_assets():
        TowerButton.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 30)
        TowerButton.images["background"] = pygame.image.load(
            get_image(images["ui"]["tower_button_background"]))

    def __render_icon(self):
        """ Render the towers icon """
        icon_image = Tower.render(self.tower_name, "model_1", 90)
        icon_image = pygame.transform.scale_by(icon_image, 0.90)
        icon_rect = icon_image.get_rect(center=(35, 40))

        self.image = TowerButton.images["background"].copy()
        self.image.blit(icon_image, icon_rect)

    def render_price(self, affordable=True):
        """ Render the towers name and price"""
        color = colors["default_font_color"]
        if not affordable:
            color = colors["not_affordable_font_color"]

        self.__draw_text(self.image, f"${self.cost}", (45, 77), color)

    def __draw_text(self, screen, text, pos, color=colors["default_font_color"]):
        font = TowerButton.fonts["default"]
        font_color = color

        text = font.render(text, True, font_color)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)
