""" Main file """
from game.game import Game


DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 576


def main():
    game = Game("grass_fields")
    game.run()


if __name__ == "__main__":
    main()
