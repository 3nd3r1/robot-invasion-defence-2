""" src/menu/menu.py """

from game.game import Game


class Menu:

    def __init__(self):
        self.__load_assets
        self.__game = None

    def __load_assets():
        return

    def start_game(self, arena):
        if self.__game:
            return self.__game

        self.__game = Game(arena)

    def run(self):
        return
