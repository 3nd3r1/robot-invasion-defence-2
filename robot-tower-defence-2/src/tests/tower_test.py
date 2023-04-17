""" src/tests/tower_test.py  """
import unittest
from game.game import Game


class TestTower(unittest.TestCase):
    """ Tests for the Towers """

    def setUp(self) -> None:
        self.test_game = Game("grass_fields")
        self.test_tower = self.test_game.create_tower("turret")

    def test_tower_placement_valid(self):
        offset = self.test_game.get_map().get_offset()
        valid_pos = (500+offset[0], 500+offset[1])

        self.assertTrue(self.test_tower.place(valid_pos))

    def test_tower_placement_out_of_map_is_invalid(self):
        invalid_pos = (0, 0)

        self.assertFalse(self.test_tower.place(invalid_pos))

    def test_tower_placement_in_water_is_invalid(self):
        offset = self.test_game.get_map().get_offset()
        invalid_pos = (380+offset[0], 380+offset[1])

        self.assertFalse(self.test_tower.place(invalid_pos))

    def test_tower_placement_in_obstacle_is_invalid(self):
        offset = self.test_game.get_map().get_offset()
        invalid_pos = (85+offset[0], 520+offset[1])

        self.assertFalse(self.test_tower.place(invalid_pos))
