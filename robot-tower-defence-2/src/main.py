""" src/main.py """
import pygame
from game.game import Game


def main():
    pygame.init()
    game = Game("grass_fields")
    game.run()


if __name__ == "__main__":
    main()
