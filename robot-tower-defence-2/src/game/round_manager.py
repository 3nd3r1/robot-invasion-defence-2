import pygame

from utils.round_generator import generate_rounds
from utils.logger import logger


class RoundManager:

    def __init__(self, game):
        self.__game = game

        self.__rounds = []

        self.__state = "spawning"

        self.__round = 1
        self.__wave = 1
        self.__robot = 1

        self.__last_round_started = 0
        self.__last_wave_started = 0
        self.__last_robot_spawned = 0

        self.__initialize_rounds()

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__game.get_arena())

    def update(self) -> None:
        time_now = pygame.time.get_ticks()

        current_round = self.__rounds[self.__round-1]
        if self.__state == "round_delay":
            if time_now-self.__last_round_started >= current_round["delay"]:
                self.__last_round_started = time_now
                self.__round += 1
                self.__wave = 1
                self.__state = "wave_delay"

        current_wave = current_round["waves"][self.__wave-1]

        if self.__state == "wave_delay":
            if time_now-self.__last_wave_started >= current_wave["delay"]:
                self.__last_wave_started = time_now
                self.__wave += 1
                self.__robot = 1
                self.__state = "spawning"

        current_robot = current_wave["robots"][self.__robot-1]

        if self.__state == "spawning":
            if time_now-self.__last_robot_spawned >= current_robot["delay"]:
                self.__last_robot_spawned = time_now
                self.__robot += 1
                if self.__robot > len(current_wave["robots"]):
                    self.__state = "wave_delay"

    def get_round(self) -> int:
        return self.__round

    def get_rounds_amount(self) -> int:
        return len(self.__rounds)
