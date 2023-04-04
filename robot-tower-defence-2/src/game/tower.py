import pygame
from utils.file_reader import get_image
from utils.config import towers


class Tower(pygame.sprite.Sprite):
    """ This class represents a tower that can be placed on the map. It has properties such as cost, range, and damage, and methods for upgrading and selling the tower. """

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.__placing = True
        self.__projectiles = pygame.sprite.Group()

    def load_image(self, tower_name: str) -> None:
        """ Load the image of the tower (this can be overwritten by child class)"""
        # Create and load the image
        base = pygame.image.load(get_image(towers["base"]))
        tower = pygame.image.load(
            get_image(towers[tower_name]["model_1"]))
        base = pygame.transform.scale_by(base, 0.25)
        tower = pygame.transform.scale_by(tower, 0.40)

        self.image.blit(base, (self.rect.width/2-base.get_width() /
                        2, self.rect.height/2-base.get_height()/2 + 15))
        self.image.blit(tower, (20, 0))

    def place(self) -> None:
        """ Place the tower on the map """
        self.__placing = False

    def draw(self, screen) -> None:
        """ Draws the tower to the screen """
        if self.__placing:
            pygame.draw.circle(screen, (50, 50, 50), self.rect.center,
                               towers[self.tower_name]["range"],  1)
        else:
            self.__projectiles.draw(screen)
        screen.blit(self.image, self.rect)

    def update(self) -> None:
        if self.__placing:
            self.rect.center = pygame.mouse.get_pos()
        else:
            self.__projectiles.update()

    def can_be_in_water(self) -> bool:
        """ Returns if the tower can be placed in water """
        return towers[self.tower_name]["can_be_in_water"]

    def on_click(self) -> None:
        """ This is called when the tower is clicked """
        pass

    def shoot(self) -> None:
        """ Creates a projectile. This is overwritten by child class"""
        pass
