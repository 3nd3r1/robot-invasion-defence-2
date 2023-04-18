from abc import abstractmethod, ABC
import pygame


class Particle(pygame.sprite.Sprite, ABC):
    def __init__(self, position):
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()

        self.rect.center = position
        super().__init__()

    def update(self):
        self._draw_particle()

    @staticmethod
    @abstractmethod
    def load_images():
        pass

    @staticmethod
    @abstractmethod
    def render_particle():
        pass

    @abstractmethod
    def _draw_particle(self):
        pass
