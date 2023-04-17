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

from game.towers.turret import Turret

from game.robots.archie import Archie
from game.robots.nathan import Nathan
from game.robots.minx import Minx


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena: str) -> None:
        self.__loading = True
        self.__running = True

        self.__screen = pygame.display.set_mode(
            (general["display_width"], general["display_height"]))
        self.__clock = pygame.time.Clock()

        self.__arena = arena
        self.__ui = Ui(self)
        self.__map = Map(arena, (188, 105))
        self.__player = Player(arenas[arena]["starting_money"])

        self.__round_manager = RoundManager(self)

        self.__new_tower = None

        self.__towers = pygame.sprite.Group()
        self.__robots = pygame.sprite.Group()
        self.__projectiles = pygame.sprite.Group()

        self.__load_images()

        self.__loading = False

    def __load_images(self) -> None:
        """ Load all images """
        # Load towers
        Turret.load_images()

        # Load robots
        Minx.load_images()
        Nathan.load_images()
        Archie.load_images()

    def spawn_robot(self, robot_type: str) -> None:
        logger.debug(f"Spawning {robot_type} ")

        if robot_type == "minx":
            self.__robots.add(Minx(self))
        elif robot_type == "nathan":
            self.__robots.add(Nathan(self))
        elif robot_type == "archie":
            self.__robots.add(Archie(self))

    def create_tower(self, tower_name) -> Tower:
        """ Create a new tower """
        if tower_name == "turret":
            self.__new_tower = Turret(self)
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

    def __on_click(self, pos) -> None:
        """ Handle click events """
        logger.debug(f"Click at {pos}")
        if self.__new_tower:
            if self.__new_tower.place(pos):
                self.__new_tower = None
            return

        self.__ui.on_click(pos)
        for tower in self.__towers:
            if tower.rect.collidepoint(pos):
                tower.on_click()

    def win_game(self) -> None:
        logger.debug("Game won!")
        self.kill()

    def run(self) -> None:
        while self.__running:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    return
                if evt.type == pygame.constants.MOUSEBUTTONDOWN:
                    self.__on_click(evt.pos)
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

    def get_map(self) -> Map:
        return self.__map

    def get_arena(self) -> str:
        return self.__arena

    def get_player(self) -> Player:
        return self.__player

    def get_towers(self) -> list:
        return self.__towers.sprites()
