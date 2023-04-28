import pygame

from utils.round_generator import generate_rounds
from utils.logger import logger


class RoundManager:

    def __init__(self, game):
        self.__game = game

        self.__rounds = []

        self.__round = 1
        self.__wave = 1
        self.__robot = 1

        self.__next_event = (0, "spawn")

        self.__initialize_rounds()

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__game.get_arena())

    def update(self) -> None:
        time_now = pygame.time.get_ticks()
        if self.__next_event[0] - time_now > 0:
            return

        evt = self.__next_event[1]

        if evt == "spawn":
            self.__spawn_robot()
        elif evt == "wave":
            self.__next_wave()
        elif evt == "round":
            self.__next_round()

    def __next_round(self):
        logger.debug(f"Round {self.__round+1} started")
        self.__round += 1
        self.__wave = 1
        self.__robot = 1

        if self.__round >= len(self.__rounds):
            self.__game.win_game()
        else:
            self.__next_event = (pygame.time.get_ticks(), "spawn")

    def __next_wave(self):
        current_round = self.__rounds[self.__round - 1]

        self.__wave += 1
        self.__robot = 1

        if self.__wave >= len(current_round["waves"]):
            self.__next_event = (pygame.time.get_ticks() + current_round["delay"], "round")
        else:
            self.__next_event = (pygame.time.get_ticks(), "spawn")

    def __spawn_robot(self):
        current_wave = self.__rounds[self.__round - 1]["waves"][self.__wave - 1]
        current_robot = current_wave["robots"][self.__robot - 1]

        self.__game.create_robot(current_robot["type"])
        self.__robot += 1

        if self.__robot >= len(current_wave["robots"]):
            self.__next_event = (pygame.time.get_ticks() + current_wave["delay"], "wave")
        else:
            self.__next_event = (pygame.time.get_ticks() + current_robot["delay"], "spawn")

    def get_round(self) -> int:
        return self.__round

    def get_rounds_amount(self) -> int:
        return len(self.__rounds)
