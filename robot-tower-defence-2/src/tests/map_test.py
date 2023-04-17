""" src/tests/map_test.py  """
import unittest
from game.game import Game


class TestMap(unittest.TestCase):
    """ Tests the Map class"""

    def setUp(self) -> None:
        self.test_game = Game("grass_fields")

    def test_tower_placement_valid(self):
        self.test_game.create_tower("turret")
        self.assertTrue(self.test_map.is_valid_tower_position(valid_tower))

    def test_tower_placement_invalid(self):
        invalid_tower = Turret()
        invalid_tower.rect.center = (200, 200)
        self.assertFalse(self.test_map.is_valid_tower_position(invalid_tower))
