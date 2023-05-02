""" src/tests/tower_test.py  """
import unittest
import pygame
from game.game import Game


class TestRobot(unittest.TestCase):
    """ Tests for the Towers """

    def setUp(self) -> None:
        pygame.init()
        self.test_game = Game("grass_fields")
        self.test_robot = self.test_game.create_robot("minx")
        self.test_tower = self.test_game.create_tower("turret")

    def test_robot_dies_and_gives_money(self):
        offset = self.test_game.map.offset
        tower_pos = (500+offset[0], 500+offset[1])
        self.test_tower.place(tower_pos)
        self.test_robot.rect.center = tower_pos

        money_before = self.test_game.player.money

        # Update game once to make tower shoot
        pygame.time.wait(1000)
        self.test_game.update()

        # Update projectiles until bullet travels to robot or 100 updates
        for _ in range(100):
            if len(self.test_game.sprites.projectiles) == 0:
                break
            self.test_game.sprites.projectiles.update()

        # Update game once to make robot die and give money
        self.test_game.update()

        # Robot should be dead
        self.assertFalse(self.test_robot.alive())

        # Check that money has increased by 1
        self.assertEqual(money_before + 1, self.test_game.player.money)

    def test_robot_reduces_players_health(self):
        health_before = self.test_game.player.health

        # Update until robot travels to end of path or 10000 updates
        for _ in range(10000):
            if not self.test_robot.alive():
                break
            self.test_robot.update()

        # Robot should be dead
        self.assertFalse(self.test_robot.alive())

        # Check that player health has decreased by 2
        self.assertEqual(health_before - 2, self.test_game.player.health)
