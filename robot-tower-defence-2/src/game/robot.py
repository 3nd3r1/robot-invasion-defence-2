import pygame
from utils.logger import logger


class Robot(pygame.sprite.Sprite):
    """This class represents a robot that moves along the map. It has properties such as speed, health, and type, and methods for moving and being damaged."""

    def __init__(self, health: int, game: "Game") -> None:
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect()

        self._walking_images = []
        self._walking_frame = 0
        self._animation_timer = 0
        self._animation_interval = 0

        self._speed = 1
        self._damage = 1

        self.__game = game
        self.__waypoints = self.__game.get_map().get_waypoints()
        self.__current_waypoint = 0
        self.__velocity = (0, 0)

        self.__health = health

        self.rect.center = self.__waypoints[self.__current_waypoint]

    def update(self) -> None:
        if self.__health <= 0 or self.__current_waypoint >= len(self.__waypoints):
            self.__game.get_player().lose_health(self._damage)
            self.kill()
            return

        self.animate()
        tx = int(self.__waypoints[self.__current_waypoint][0])
        ty = int(self.__waypoints[self.__current_waypoint][1])
        self.__velocity = (min(max(tx-self.rect.centerx, -self._speed), self._speed),
                           min(max(ty-self.rect.centery, -self._speed), self._speed))
        self.rect.move_ip(self.__velocity)
        if self.__velocity == (0, 0):
            self.__current_waypoint += 1

    def animate(self) -> None:
        """This method animates the robot's walking. It can be overridden by subclasses to add more animations."""
        if self._animation_timer < self._animation_interval:
            self._animation_timer += 1
            return

        self._animation_timer = 0

        if self.__velocity[0] == 0 and self.__velocity[1] < 0:
            if self._walking_frame > 6:
                self._walking_frame = 0
            else:
                self._walking_frame += 1
        elif self.__velocity[0] < 0 and self.__velocity[1] == 0:
            if self._walking_frame > 14 or self._walking_frame < 8:
                self._walking_frame = 8
            else:
                self._walking_frame += 1
        elif self.__velocity[0] == 0 and self.__velocity[1] > 0:
            if self._walking_frame > 22 or self._walking_frame < 16:
                self._walking_frame = 16
            else:
                self._walking_frame += 1
        else:
            if self._walking_frame > 30 or self._walking_frame < 24:
                self._walking_frame = 24
            else:
                self._walking_frame += 1

        self.image = self._walking_images[self._walking_frame].copy()

    def lose_health(self, amount: int) -> None:
        """This method decreases the robot's health by the given amount."""
        self.__health -= amount
        if self.__health <= 0:
            self.kill()
