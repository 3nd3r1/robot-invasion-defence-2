import pygame


class Robot(pygame.sprite.Sprite):
    """This class represents a robot that moves along the map. It has properties such as speed, health, and type, and methods for moving and being damaged."""

    def __init__(self, health: int, map: "Map") -> None:
        super().__init__()
        self.image = pygame.Surface((100, 200))
        self.rect = self.image.get_rect()

        self.__map = map
        self.__current_path = 0
        self.__velocity = (0, 0)

        self.__health = health
        self.__alive = True

    def update(self) -> None:
        if self.__health <= 0 or self.__current_path >= len(self.__path):
            self.__alive = False
        if self.__alive:
            tx = self.__path[self.__current_path].centerx
            ty = self.__path[self.__current_path].centery
            self.__velocity = (min(max(tx-self.rect.centerx, -1), 1),
                               min(max(ty-self.rect.centery, -1), 1))
            self.rect.move(self.__velocity)
            if self.__velocity == (0, 0):
                self.__current_path += 1

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
