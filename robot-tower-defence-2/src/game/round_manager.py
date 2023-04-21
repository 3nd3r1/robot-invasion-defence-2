import pygame

from utils.round_generator import generate_rounds
from utils.logger import logger


class RoundManager:

    def __init__(self, game):
        self.__game = game

        self.__last_robot = {"start_time": 0, "delay": 0}
        self.__last_wave = {"start_time": 0, "delay": 0}
        self.__last_round = {"start_time": 0, "delay": 0}

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

        if time_now-self.__last_round["start_time"] < self.__last_round["delay"]:
            return

        if time_now-self.__last_wave["start_time"] < self.__last_wave["delay"]:
            return

        if time_now-self.__last_robot["start_time"] < self.__last_robot["delay"]:
            return

        self.__game.create_robot(current_robot["type"])
        self.__robot += 1
        self.__last_robot = {"start_time": time_now, "delay": current_robot["spawn_delay"]}

        if self.__robot > len(current_wave["robots"]):
            self.__robot = 1
            self.__wave += 1
            self.__last_wave = {"start_time": time_now, "delay": current_wave["wave_delay"]}

        if self.__wave > len(current_round["waves"]):
            self.__wave = 1
            self.__round += 1
            self.__last_round = {"start_time": time_now, "delay": current_round["round_delay"]}
            logger.debug(
                f"Round {self.__round-1} finished new round: {self.__round}")

    def get_round(self) -> int:
        return self.__round

    def get_rounds_amount(self) -> int:
        return len(self.__rounds)
