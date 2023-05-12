""" src/tests/tower_test.py  """
import unittest
import pygame
from game.game import Game
from utils.db import reset_player


class TestGame(unittest.TestCase):
    """ Tests for the Towers """

    def setUp(self) -> None:
        pygame.init()
        reset_player()  # Reset the player's save

        self.test_game = Game("grass_fields", False)
        self.__create_test_towers()
        self.__create_test_robots()
        self.test_game.player.earn_money(50)
        self.test_game.player.lose_health(20)

    def __create_test_towers(self):
        self.test_game.create_tower("turret").place((400, 175))
        self.test_game.create_tower("missile_launcher").place((540, 175))
        self.test_game.create_tower("cannon").place((700, 175))

    def __create_test_robots(self):
        self.test_game.create_robot("minx")
        self.test_game.create_robot("nathan")
        self.test_game.create_robot("archie")

    def test_creating_save_and_loading_save(self):
        # Kill the game to save the game
        self.test_game.kill()

        # Create a new game and load the save
        new_game = Game("grass_fields", True)

        # Check that nothing has changed
        self.assertEqual(new_game.player.money, 300)
        self.assertEqual(new_game.player.health, 80)
        self.assertEqual(len(new_game.sprites.towers), 3)
        self.assertEqual(len(new_game.sprites.robots), 3)

        # Check that game still works
        new_game.update()

    def test_dying_results_in_losing_game(self):

        self.test_game.update()
        self.assertEqual(self.test_game.player.health, 80)
        self.assertEqual(self.test_game.player.alive, True)
        self.assertEqual(self.test_game.state.state, "game")

        self.test_game.player.lose_health(80)
        self.test_game.update()

        self.assertEqual(self.test_game.player.health, 0)
        self.assertEqual(self.test_game.player.alive, False)
        self.assertEqual(self.test_game.state.state, "lose")
