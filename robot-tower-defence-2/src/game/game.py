""" Main game file """
from utils.round_generator import generate_rounds


class Game:
    """" This class represents the game itself and contains all other classes. """

    def __init__(self, arena: str) -> None:
        self.__round = 1
        self.__loading = True
        self.__paused = True
        self.__arena = arena

        self.__towers = []
        self.__robots = []
        self.__rounds = []

        self.__initialize_rounds()
        self.__loading = False

    def next_round(self) -> None:
        self.__round += 1

    def __initialize_rounds(self) -> None:
        self.__rounds = generate_rounds(self.__arena)
