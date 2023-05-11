import dataclasses
import pygame

from utils.round_generator import generate_rounds
from utils.logger import logger


@dataclasses.dataclass
class Event:
    time: int
    type: str


class RoundManager:

    def __init__(self, game):
        self.__game = game

        self.__rounds = []

        self.__round = 1
        self.__wave = 1
        self.__robot = 1

        self.__next_event = Event(0, "spawn")

        self.__initialize_rounds()

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_RoundManager__game"] = None
        state["_RoundManager__next_event"].time -= pygame.time.get_ticks()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__next_event.time += pygame.time.get_ticks()

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__game.map.arena)

    def reset(self) -> None:
        self.__round = 1
        self.__wave = 1
        self.__robot = 1
        self.__next_event = Event(0, "spawn")

    def update(self) -> None:
        time_now = pygame.time.get_ticks()
        if self.__next_event.time - time_now > 0:
            return

        evt = self.__next_event.type

        if evt == "spawn":
            self.__spawn_robot()
        elif evt == "wave":
            self.__next_wave()
        elif evt == "round":
            self.next_round()
        elif evt == "wait_for_win":
            if len(self.__game.sprites.robots) == 0:
                self.__game.win_game()

    def next_round(self):
        logger.debug(f"Round {self.__round+1} started")
        self.__round += 1
        self.__wave = 1
        self.__robot = 1

        if self.__round >= len(self.__rounds):
            self.__next_event = Event(pygame.time.get_ticks(), "wait_for_win")
        else:
            self.__next_event = Event(pygame.time.get_ticks(), "spawn")

    def __next_wave(self):
        current_round = self.__rounds[self.__round - 1]

        self.__wave += 1
        self.__robot = 1

        if self.__wave >= len(current_round["waves"]):
            self.__next_event = Event(pygame.time.get_ticks() + current_round["delay"], "round")
        else:
            self.__next_event = Event(pygame.time.get_ticks(), "spawn")

    def __spawn_robot(self):
        current_wave = self.__rounds[self.__round - 1]["waves"][self.__wave - 1]
        current_robot = current_wave["robots"][self.__robot - 1]

        self.__game.create_robot(current_robot["type"])
        self.__robot += 1

        if self.__robot >= len(current_wave["robots"]):
            self.__next_event = Event(pygame.time.get_ticks() + current_wave["delay"], "wave")
        else:
            self.__next_event = Event(pygame.time.get_ticks() + current_robot["delay"], "spawn")

    @property
    def round(self) -> int:
        return self.__round

    @property
    def rounds_amount(self) -> int:
        return len(self.__rounds)
