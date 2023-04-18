""" src/game/game.py """
import pygame

from utils.config import general, arenas
from utils.logger import logger
from utils.math import distance_between_points

from game.map import Map
from game.round_manager import RoundManager

from game.ui import Ui
from game.player import Player
from game.tower import Tower
from game.robot import Robot

from game.towers import Turret, MissileLauncher, Cannon
from game.robots import Minx, Nathan, Archie


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena: str) -> None:
        self.__loading = True
        self.__running = True

        flags = pygame.constants.NOFRAME
        starting_money = arenas[arena]["starting_money"]

        if general["debug"]:
            flags = 0
            starting_money = 100000

        self.__screen = pygame.display.set_mode(
            (general["display_width"], general["display_height"]), flags)
        self.__clock = pygame.time.Clock()

        self.__load_images()

        self.__arena = arena
        self.__ui = Ui(self)
        self.__map = Map(arena, (188, 105))
        self.__player = Player(starting_money)

        self.__round_manager = RoundManager(self)

        self.__new_tower = None

        self.__towers = pygame.sprite.Group()
        self.__robots = pygame.sprite.Group()
        self.__projectiles = pygame.sprite.Group()

        self.__loading = False

    def __load_images(self) -> None:
        """ Load all images """
        # Load towers
        Turret.load_images()
        MissileLauncher.load_images()
        Cannon.load_images()

        # Load robots
        Minx.load_images()
        Nathan.load_images()
        Archie.load_images()

    def create_robot(self, robot_name) -> Robot:
        """ Create a new robot """

        new_robot = None

        if robot_name == "minx":
            new_robot = Minx(self)
        elif robot_name == "nathan":
            new_robot = Nathan(self)
        elif robot_name == "archie":
            new_robot = Archie(self)

        if new_robot:
            self.__robots.add(new_robot)

        return new_robot

    def create_tower(self, tower_name) -> Tower:
        """ Create a new tower """
        if tower_name == "turret":
            self.__new_tower = Turret(self)
        elif tower_name == "missile_launcher":
            self.__new_tower = MissileLauncher(self)
        elif tower_name == "cannon":
            self.__new_tower = Cannon(self)

        return self.__new_tower

    def add_projectile(self, projectile):
        self.__projectiles.add(projectile)

    def add_tower(self, tower):
        self.__towers.add(tower)

    def update(self) -> None:
        """ Update all game objects """
        if self.__loading:
            return

        if self.__new_tower:
            self.__new_tower.update()

        self.__round_manager.update()

        self.__projectiles.update()
        self.__towers.update()
        self.__robots.update()

    def draw(self, screen) -> None:
        """ Draw all game objects """
        screen.fill((0, 0, 0))
        self.__map.draw(screen)
        self.__projectiles.draw(screen)
        self.__towers.draw(screen)
        self.__robots.draw(screen)
        self.__ui.draw(screen)

        if self.__new_tower:
            self.__new_tower.draw(screen)

    def __on_click(self, pos, button) -> None:
        """ Handle click events """
        logger.debug(f"Click at {pos}")

        if self.__new_tower and button == 1:
            self.__place_tower(pos)
            return

        if self.__new_tower and button == 3:
            self.__new_tower = None

        self.__ui.on_click(pos)

        for tower in self.__towers:
            if tower.rect.collidepoint(pos):
                tower.on_click()

    def win_game(self) -> None:
        logger.debug("Game won!")
        self.kill()

    def run(self):
        while self.__running:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    return
                if evt.type == pygame.constants.MOUSEBUTTONDOWN:
                    self.__on_click(evt.pos, evt.button)
            self.update()
            self.draw(self.__screen)
            pygame.display.flip()
            self.__clock.tick(general["fps"])

    def kill(self) -> None:
        self.__running = False
        self.__towers.empty()
        self.__projectiles.empty()
        self.__robots.empty()

    def get_closest_robot_in_range(self, tower):
        """ Get the closest robot to the tower """
        closest_robot = None
        for robot in self.__robots:
            new_distance = distance_between_points(
                robot.rect.center, tower.rect.center)
            old_distance = distance_between_points(
                closest_robot.rect.center, tower.rect.center) if closest_robot else 999999
            if new_distance <= tower.get_range() and new_distance < old_distance:
                closest_robot = robot

        return closest_robot

    def __place_tower(self, pos):
        if not self.__new_tower:
            return

        if self.get_player().get_money() < self.__new_tower.get_cost():
            return

        if self.__new_tower.place(pos):
            self.get_player().spend_money(self.__new_tower.get_cost())
            self.__new_tower = None

    def get_map(self) -> Map:
        return self.__map

    def get_arena(self) -> str:
        return self.__arena

    def get_player(self) -> Player:
        return self.__player

    def get_towers(self) -> list:
        return self.__towers.sprites()

    def get_projectiles(self) -> list:
        return self.__projectiles.sprites()

    def get_robots(self) -> list:
        return self.__robots.sprites()
