""" src/game/game.py """
import pickle
import dataclasses
import pygame

from utils.config import general, arenas
from utils.logger import logger
from utils.math import distance_between_points
from utils import db

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

    def __getstate__(self):
        """ This is called when the game sprites are being pickled """
        state = self.__dict__.copy()
        state["new_tower"] = None
        state["towers"] = state["towers"].sprites()
        state["robots"] = state["robots"].sprites()
        state["projectiles"] = state["projectiles"].sprites()
        state["particles"] = state["particles"].sprites()
        return state

    def __setstate__(self, state):
        """ This is called when the game sprites are being unpickled """
        self.new_tower = None
        self.towers = TowerGroup()
        self.robots = RobotGroup()
        self.projectiles = ProjectileGroup()
        self.particles = ParticleGroup()

        for tower in state["towers"]:
            self.towers.add(tower)

        for robot in state["robots"]:
            self.robots.add(robot)

        for projectile in state["projectiles"]:
            self.projectiles.add(projectile)

        for particle in state["particles"]:
            self.particles.add(particle)

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
    """" This class represents the game itself and contains all other classes.

     Attributes:
            state (GameState): The current state of the game.
            clock (pygame.time.Clock): The game clock.
            screen (pygame.Surface): The game screen.
            game_ui (GameUi): The game ui.
            map (Map): The game map.
            player (Player): The player.
            round_manager (RoundManager): The round manager.
            sprites (GameSprites): The game sprites.

    """

    def __init__(self, arena, load_save=False) -> None:
        self.__state = GameState()

        starting_money = arenas[arena]["starting_money"]
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(
            (general["screen_width"], general["screen_height"]))

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

        if load_save:
            self.load_save()

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

        if not self.player.alive:
            self.lose_game()
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
        self.state.state = "win"
        db.add_player_experience(arenas[self.map.arena]["experience_reward"])
        db.add_player_score(self.map.arena, self.round_manager.round)

    def lose_game(self):
        logger.debug("Game lost!")
        self.state.state = "lose"
        db.add_player_score(self.map.arena, self.round_manager.round)

    def pause_game(self):
        logger.debug("Game paused!")
        self.sprites.new_tower = None
        self.state.state = "pause"

    def unpause_game(self):
        logger.debug("Game unpaused!")
        self.state.state = "game"

    def restart_game(self):
        logger.debug("Game restarted!")
        self.state.state = "loading"
        self.state.running = True

        self.sprites.empty()
        self.player.reset()
        self.round_manager.reset()

        self.state.state = "game"

    def run(self):
        while self.state.running:
            self.__event_loop()
            self.update()
            self.draw(self.__screen)
            pygame.display.flip()
            self.__clock.tick(general["fps"])

    def __event_loop(self):
        for evt in pygame.event.get():
            if evt.type == pygame.constants.QUIT:
                self.kill("quit")
            if evt.type == pygame.constants.MOUSEBUTTONDOWN:
                self.__on_click(evt.pos, evt.button)
            if evt.type == pygame.constants.KEYDOWN:
                if evt.key == pygame.constants.K_ESCAPE:
                    self.pause_game()

                # Debug keys
                if not general["debug"]:
                    continue
                if evt.key == pygame.constants.K_F1:
                    self.round_manager.next_round()
                if evt.key == pygame.constants.K_F2:
                    self.player.earn_money(9999999999)

    def save(self):
        """ Save the game state to the database """

        logger.debug("Saving game state")
        sprites_data = pickle.dumps(self.sprites)
        player_data = pickle.dumps(self.player)
        rounds_data = pickle.dumps(self.round_manager)

        db.add_game_save(self.map.arena, self.round_manager.round,
                         sprites_data, player_data, rounds_data)

    def load_save(self):
        """ Load the game state from the database """
        self.state.state = "loading"
        save = db.get_game_save(self.map.arena)
        if not save:
            return

        self.__sprites = pickle.loads(save["sprites_data"])
        self.__player = pickle.loads(save["player_data"])
        self.__round_manager = pickle.loads(save["rounds_data"])

        # I have no idea if this is good workaround or a terrible idea

        for tower in self.sprites.towers:
            tower.__dict__.update({"_Tower__game": self})
        for robot in self.sprites.robots:
            robot.__dict__.update({"_Robot__game": self})

        self.round_manager.__dict__.update({"_RoundManager__game": self})

        self.state.state = "game"

    def kill(self, kill_state="dead") -> None:
        """ Kill the game instance """
        logger.debug("Killing game instance")

        # Delete old save and save game if the game is not over
        db.delete_game_save(self.map.arena)
        if self.state.state not in ("win", "lose"):
            self.save()

        self.state.state = kill_state
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
