import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
