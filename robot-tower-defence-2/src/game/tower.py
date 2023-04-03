import pygame

class Tower(pygame.sprite.Sprite):
    """ This class represents a tower that can be placed on the map. It has properties such as cost, range, and damage, and methods for upgrading and selling the tower. """

    def __init__(self) -> None:
        self.__pos = ()
        self.__placing = True
        self.__projectiles = pygame.sprite.Group()

    def draw(self, screen) -> None:
        self.__projectiles.draw(screen)
    
    def update(self) -> None:
        self.__projectiles.update()
    
    def __shoot(self) -> None:
        """ Creates a projectile. This is overwritten by child class"""
        pass