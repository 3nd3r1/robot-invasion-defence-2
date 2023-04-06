""" src/game/game.py """
import pygame
from utils.round_generator import generate_rounds
from utils.config import general
from utils.logger import logger
from utils.math import distance_between_points
from game.robots.mech import Mech
from game.map import Map
from game.ui import Ui
from game.player import Player
from game.towers.turret import Turret


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena: str) -> None:
        self.__loading = True
        self.__paused = False
        self.__new_tower = None
        self.__screen = pygame.display.set_mode(
            (general["display_width"], general["display_height"]))
        self.__clock = pygame.time.Clock()
        self.__arena = arena

        self.__ui = Ui(self)
        self.__map = Map(arena, 188, 105)
        self.__player = Player()

        self.__towers = pygame.sprite.Group()
        self.__robots = pygame.sprite.Group()
        self.__projectiles = pygame.sprite.Group()

        self.__round = 1
        self.__rounds = []

        self.__initialize_rounds()
        self.__loading = False

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__arena)

    def next_round(self) -> None:
        self.__round += 1

    def spawn_robot(self, robot: dict) -> None:
        if robot["type"] == "mech":
            self.__robots.add(
                Mech(robot["health"], self))

    def place_tower(self) -> None:
        """ Place a tower on the map """
        for tower in self.__towers:
            if tower.rect.collidepoint(self.__new_tower.rect.center):
                logger.debug("Tower collides with another tower")
                return
        if self.__map.is_valid_tower_position(self.__new_tower):
            self.__new_tower.place()
            self.__towers.add(self.__new_tower)
            self.__new_tower = None

    def create_tower(self, tower_name: str) -> None:
        """ Create a new tower """
        if tower_name == "turret":
            self.__new_tower = Turret(self)

    def add_projectile(self, projectile: "Projectile") -> None:
        self.__projectiles.add(projectile)

    def update(self) -> None:
        if self.__new_tower:
            self.__new_tower.update()
        self.__projectiles.update()
        self.__towers.update()
        self.__robots.update()

    def draw(self, screen) -> None:
        self.__map.draw(screen)
        self.__projectiles.draw(screen)
        self.__robots.draw(screen)
        self.__towers.draw(screen)
        self.__ui.draw(screen)

        if self.__new_tower:
            self.__new_tower.draw(screen)

    def __on_click(self, pos) -> None:
        """ Handle click events """
        logger.debug(f"Click at {pos}")
        if self.__new_tower:
            self.place_tower()
            return
        self.__ui.on_click(pos)
        for tower in self.__towers:
            if tower.rect.collidepoint(pos):
                tower.on_click()

    def run(self) -> None:
        while not self.__paused:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    return
                if evt.type == pygame.constants.MOUSEBUTTONDOWN:
                    self.__on_click(evt.pos)
                if evt.type == pygame.constants.KEYDOWN:
                    self.spawn_robot(
                        {"type": "mech", "health": 2})
            self.update()
            self.draw(self.__screen)
            pygame.display.flip()
            self.__clock.tick(general["fps"])

    def get_closest_robot_in_range(self, tower: "Tower") -> "Robot" or None:
        """ Get the closest robot to the tower """
        for robot in self.__robots:
            if distance_between_points(robot.rect.center, tower.rect.center) <= tower.get_range():
                return robot
        return None

    def get_map(self) -> Map:
        return self.__map

    def get_player(self) -> Player:
        return self.__player
