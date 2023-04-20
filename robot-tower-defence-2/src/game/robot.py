from abc import ABC, abstractmethod
import pygame

from utils.logger import logger
from utils.math import get_angle


class Robot(pygame.sprite.Sprite, ABC):
    """
    This class represents a robot that moves along the map.
    It has properties such as speed, health, and type,
    and methods for moving and being damaged.
    """

    def __init__(self, game, health: int) -> None:
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect()

        self.__velocity = (0, 0)
        self.__health = health

        self.__game = game

        self.__waypoints = iter(self.__get_waypoints())
        self.__current_waypoint = next(self.__waypoints)

        self.rect.center = self.__current_waypoint

        logger.debug(f"Robot ({id(self)}) created with {self.get_health()} HP")

    def __get_waypoints(self) -> list:
        waypoints = self.__game.get_map().get_waypoints()
        offset_waypoints = []

        for i, waypoint in enumerate(waypoints[:-1]):
            difference_x = waypoints[i+1][0] - waypoint[0]
            difference_y = waypoints[i+1][1] - waypoint[1]

            path_offset = self.get_path_offset().rotate(get_angle(difference_x, difference_y))
            offset_waypoints.append((round(waypoint[0]+path_offset[0]),
                                    round(waypoint[1]+path_offset[1])))
        offset_waypoints.append(waypoints[-1])

        return offset_waypoints

    def update(self) -> None:
        if self.get_health() <= 0:
            self.__game.get_player().earn_money(self.get_bounty())
            logger.debug(f"Robot ({id(self)}) died")
            self.kill()
            return

        if not self.__current_waypoint:
            self.__game.get_player().lose_health(self.get_damage())
            logger.debug(f"Robot ({id(self)}) reached the end of the map")
            self.kill()
            return

        self.__calculate_velocity()
        self.rect.move_ip(self.get_velocity())

        self._draw_robot()

        if self.get_velocity() == (0, 0):
            self.__current_waypoint = next(self.__waypoints, None)

    def __calculate_velocity(self):
        waypoint_x = self.__current_waypoint[0]
        waypoint_y = self.__current_waypoint[1]

        velocity_x = min(max(waypoint_x-self.rect.move(self.rect.width//2 +
                         self.get_path_offset()[0], 0).left, -self.get_speed()), self.get_speed())
        velocity_y = min(max(waypoint_y-self.rect.move(0, self.rect.height +
                         self.get_path_offset()[1]).top, -self.get_speed()), self.get_speed())

        self.__velocity = (velocity_x, velocity_y)

    def lose_health(self, amount: int) -> None:
        """This method decreases the robot's health by the given amount."""
        self.__health = self.__health - amount

    def get_health(self) -> int:
        """This method returns the robot's health."""
        return self.__health

    def get_velocity(self) -> tuple:
        """This method returns the robot's velocity."""
        return self.__velocity

    @staticmethod
    @abstractmethod
    def load_images():
        pass

    @staticmethod
    @abstractmethod
    def render_robot(frame: int) -> pygame.Surface:
        pass

    @abstractmethod
    def _draw_robot(self) -> None:
        pass

    @abstractmethod
    def get_damage(self) -> int:
        pass

    @abstractmethod
    def get_bounty(self) -> int:
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_path_offset(self) -> pygame.math.Vector2:
        pass
