""" src/game/ui_components/tower_button.py """
import pygame
from utils.config import towers
from utils.file_reader import get_image
from game.tower import Tower
from game.towers.turret import Turret


class TowerButton(pygame.sprite.Sprite):
    """ Tower button class """

    def __init__(self, tower: str, pos: tuple) -> None:
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.constants.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.tower_name = tower

        self.__render_icon()

    def __render_icon(self):
        """ Render the towers icon """
        base = pygame.image.load(get_image(towers["base"]))
        tower = pygame.image.load(
            get_image(towers[self.tower_name]["model_1"]))
        base = pygame.transform.scale_by(base, 0.25)
        tower = pygame.transform.scale_by(tower, 0.40)

        self.image.blit(base, (self.rect.width/2-base.get_width() /
                        2,   self.rect.height/2-base.get_height()/2 + 15))
        self.image.blit(tower, (20, 0))

    def on_click(self):
        pass
