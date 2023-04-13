import pygame

from utils.round_generator import generate_rounds
from utils.logger import logger


class RoundManager:

    def __init__(self, game: "Game"):
        self.__game = game

        self.__last_spawn = 0
        self.__last_wave = 0
        self.__last_round = 0

        self.__rounds = []

        self.__round = 1
        self.__wave = 1
        self.__robot = 1

        self.__initialize_rounds()

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__game.get_arena())

    def update(self) -> None:
        if self.__round > len(self.__rounds):
            self.__game.win_game()

        current_round = self.__rounds[self.__round-1]
        current_wave = current_round["waves"][self.__wave-1]
        current_robot = current_wave["robots"][self.__robot-1]
        time_now = pygame.time.get_ticks()

        if time_now-self.__last_round < current_round["round_delay"]:
            return

        if time_now-self.__last_wave < current_round["wave_interval"]:
            return

        if time_now-self.__last_spawn < current_wave["spawn_interval"]:
            return

        self.__game.spawn_robot(current_robot["type"])
        self.__robot += 1
        self.__last_spawn = time_now

        if self.__robot > len(current_wave["robots"]):
            self.__robot = 1
            self.__last_wave = time_now
            self.__wave += 1

        if self.__wave > len(current_round["waves"]):
            self.__wave = 1
            self.__last_round = time_now
            self.__round += 1
            logger.debug(
                f"Round {self.__round-1} finished new round: {self.__round}")
