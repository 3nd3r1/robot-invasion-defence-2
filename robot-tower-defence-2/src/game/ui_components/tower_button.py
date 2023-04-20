""" src/game/ui_components/tower_button.py """
import pygame
from game.towers import Turret, MissileLauncher, Cannon


class TowerButton(pygame.sprite.Sprite):
    """ Tower button class """

    def __init__(self, tower, pos):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.constants.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.tower_name = tower

        self.__render_icon()
        self.__render_price()

    def __render_icon(self):
        """ Render the towers icon """
        if self.tower_name == "turret":
            icon_image = Turret.render_tower(0)
        elif self.tower_name == "missile_launcher":
            icon_image = MissileLauncher.render_tower(0)
        elif self.tower_name == "cannon":
            icon_image = Cannon.render_tower(0)

        icon_rect = icon_image.get_rect(center=(50, 60))
        self.image.blit(icon_image, icon_rect)

    def __render_price(self):
        """ Render the towers name and price"""
        return

    def on_click(self):
        return
