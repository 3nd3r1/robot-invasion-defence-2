from abc import abstractmethod, ABC
import pygame


class Particle(pygame.sprite.Sprite, ABC):
    def __init__(self, position):
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()

        self.rect.center = position

    def update(self):
        self._draw_particle()

    @staticmethod
    @abstractmethod
    def load_images():
        pass

    @staticmethod
    @abstractmethod
    def render_projectile():
        pass

    @abstractmethod
    def _draw_particle(self):
        pass
