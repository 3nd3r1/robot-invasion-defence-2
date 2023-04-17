""" src/tests/tower_test.py  """
import unittest
import pygame
from game.game import Game


class TestRobot(unittest.TestCase):
    """ Tests for the Towers """

    def setUp(self) -> None:
        self.test_game = Game("grass_fields")
        self.test_robot = self.test_game.create_robot("minx")
