import pygame


class Robot(pygame.sprite.Sprite):
    """This class represents a robot that moves along the map. It has properties such as speed, health, and type, and methods for moving and being damaged."""

    def __init__(self, health: int, _map: "Map") -> None:
        super().__init__()
        self.image = pygame.Surface((100, 200))
        self.rect = self.image.get_rect()

        self.__map = _map
        self.__waypoints = self.__map.get_waypoints()
        self.__current_waypoint = 0
        self.__velocity = (0, 0)

        self.__health = health
        self.__alive = True

        self.rect.center = self.__waypoints[self.__current_waypoint]

    def update(self) -> None:
        if self.__health <= 0 or self.__current_waypoint >= len(self.__waypoints):
            self.__alive = False
        if self.__alive:
            tx = self.__waypoints[self.__current_waypoint][0]
            ty = self.__waypoints[self.__current_waypoint][1]
            self.__velocity = (min(max(tx-self.rect.centerx, -1), 1),
                               min(max(ty-self.rect.centery, -1), 1))
            self.rect.move_ip(self.__velocity)
            if self.__velocity == (0, 0):
                self.__current_waypoint += 1

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
