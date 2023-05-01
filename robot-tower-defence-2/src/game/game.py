""" src/game/game.py """
import dataclasses
import pygame

from utils.config import general, arenas
from utils.logger import logger
from utils.math import distance_between_points

from ui.game_ui import GameUi

from game.map import Map
from game.round_manager import RoundManager

from game.player import Player

from game.tower import Tower, TowerGroup
from game.robot import Robot, RobotGroup
from game.particle import Particle, ParticleGroup
from game.projectile import Projectile, ProjectileGroup

from game.towers import Turret, MissileLauncher, Cannon
from game.robots import Minx, Nathan, Archie


@dataclasses.dataclass
class GameState:
    state: str = "loading"
    running: bool = True


@dataclasses.dataclass
class GameSprites:
    new_tower: Tower
    towers: pygame.sprite.Group
    robots: pygame.sprite.Group
    projectiles: pygame.sprite.Group
    particles: pygame.sprite.Group

    def update(self):
        self.towers.update()
        self.robots.update()
        self.projectiles.update()
        self.particles.update()

    def draw(self, screen):
        self.projectiles.draw(screen)
        self.towers.draw(screen)
        self.robots.draw(screen)
        self.particles.draw(screen)

    def empty(self):
        self.new_tower = None
        self.towers.empty()
        self.robots.empty()
        self.projectiles.empty()
        self.particles.empty()


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena) -> None:
        self.__state = GameState()

        starting_money = arenas[arena]["starting_money"]

        if general["debug"]:
            starting_money = 100000

        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((general["screen_width"], general["screen_height"]))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.__load_assets()

        self.__game_ui = GameUi(self)
        self.__map = Map(arena, (188, 120))
        self.__player = Player(starting_money)
        self.__round_manager = RoundManager(self)

        self.__sprites = GameSprites(
            new_tower=None,
            towers=TowerGroup(),
            robots=RobotGroup(),
            projectiles=ProjectileGroup(),
            particles=ParticleGroup()
        )

        self.__state.state = "game"

    def __load_assets(self) -> None:
        """ Load all assets """

        # Load ui
        GameUi.load_assets()

        # Load sprite assets
        Tower.load_assets()
        Robot.load_assets()
        Particle.load_assets()
        Projectile.load_assets()

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
            self.sprites.robots.add(new_robot)

        return new_robot

    def create_tower(self, tower_name) -> Tower:
        """ Create a new tower """
        if tower_name == "turret":
            self.sprites.new_tower = Turret(self)
        elif tower_name == "missile_launcher":
            self.sprites.new_tower = MissileLauncher(self)
        elif tower_name == "cannon":
            self.sprites.new_tower = Cannon(self)

        return self.sprites.new_tower

    def update(self) -> None:
        """ Update all game objects """
        if self.state.state != "game":
            return

        if self.sprites.new_tower:
            self.sprites.new_tower.update()

        self.round_manager.update()
        self.sprites.update()

    def draw(self, screen) -> None:
        """ Draw all game objects """
        screen.fill((0, 0, 0))

        self.map.draw(screen)
        self.sprites.draw(screen)
        self.__game_ui.draw(screen)

        if self.sprites.new_tower and self.state.state == "game":
            self.sprites.new_tower.draw(screen)

    def __on_click(self, pos, button) -> None:
        """ Handle click events """
        logger.debug(f"Click at {pos}")

        if self.sprites.new_tower and button == 1:
            self.__place_tower(pos)
            return

        if self.sprites.new_tower and button == 3:
            self.sprites.new_tower = None

        self.__game_ui.on_click(pos)
        self.sprites.towers.on_click(pos)

    def __place_tower(self, pos):
        """ Places the new tower at the given position """
        if not self.sprites.new_tower:
            return

        if self.player.money < self.sprites.new_tower.cost:
            return

        if self.sprites.new_tower.place(pos):
            self.player.spend_money(self.sprites.new_tower.cost)
            self.sprites.new_tower = None

    def win_game(self):
        logger.debug("Game won!")
        self.state.state = "won"
        self.kill()

    def lose_game(self):
        logger.debug("Game lost!")
        self.state.state = "lost"
        self.kill()

    def pause_game(self):
        logger.debug("Game paused!")
        self.state.state = "pause"

    def unpause_game(self):
        logger.debug("Game unpaused!")
        self.state.state = "game"

    def run(self):
        while self.state.running:
            for evt in pygame.event.get():
                if evt.type == pygame.constants.QUIT:
                    pygame.quit()
                if evt.type == pygame.constants.MOUSEBUTTONDOWN:
                    self.__on_click(evt.pos, evt.button)
            self.update()
            self.draw(self.__screen)
            pygame.display.flip()
            self.__clock.tick(general["fps"])

    def kill(self) -> None:
        self.state.state = "dead"
        self.state.running = False

        self.sprites.empty()

    def get_closest_robot_in_range(self, tower):
        """ Get the closest robot to the tower """
        closest_robot = None
        for robot in self.sprites.robots:
            new_distance = distance_between_points(
                robot.rect.center, tower.rect.center)
            old_distance = distance_between_points(
                closest_robot.rect.center, tower.rect.center) if closest_robot else 999999
            if new_distance <= tower.range and new_distance < old_distance:
                closest_robot = robot

        return closest_robot

    @property
    def map(self) -> Map:
        return self.__map

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def round_manager(self) -> RoundManager:
        return self.__round_manager

    @property
    def sprites(self) -> GameSprites:
        return self.__sprites

    @property
    def state(self) -> str:
        return self.__state
