""" src/tests/map_test.py  """
import unittest
import pygame
from game.map import Map
from game.towers.turret import Turret


class TestMap(unittest.TestCase):
    """ Tests the Map class"""

    def setUp(self) -> None:
        pygame.display.set_mode((1280, 720))
        self.test_map = Map("grass_fields", 0, 0)

    def test_tower_placement_valid(self):
        valid_tower = Turret()
        valid_tower.rect.center = (500, 500)
        self.assertTrue(self.test_map.is_valid_tower_position(valid_tower))

    def test_tower_placement_invalid(self):
        invalid_tower = Turret()
        invalid_tower.rect.center = (200, 200)
        self.assertFalse(self.test_map.is_valid_tower_position(invalid_tower))
