""" src/tests/tower_test.py  """
import unittest
import pygame
from game.game import Game


class TestTower(unittest.TestCase):
    """ Tests for the Towers """

    def setUp(self) -> None:
        pygame.init()
        self.test_game = Game("grass_fields")
        self.test_tower = self.test_game.create_tower("turret")
        self.test_robot = self.test_game.create_robot("minx")

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

    def test_tower_placement_in_path_is_invalid(self):
        offset = self.test_game.get_map().get_offset()
        invalid_pos = (210+offset[0], 620+offset[1])

        self.assertFalse(self.test_tower.place(invalid_pos))

    def test_tower_placement_in_tower_is_invalid(self):
        offset = self.test_game.get_map().get_offset()
        pos = (500+offset[0], 500+offset[1])
        self.test_tower.place(pos)

        other_tower = self.test_game.create_tower("turret")

        self.assertFalse(other_tower.place(pos))

    def test_tower_targets_robot_in_range(self):
        offset = self.test_game.get_map().get_offset()
        tower_pos = (500+offset[0], 500+offset[1])
        robot_pos = (594+offset[0], 522+offset[1])
        self.test_tower.place(tower_pos)
        self.test_robot.rect.center = robot_pos

        # Does tower target robot?
        self.test_game.update()
        self.assertEqual(self.test_tower.get_target(), self.test_robot)

    def test_tower_shoots_at_target(self):
        offset = self.test_game.get_map().get_offset()
        tower_pos = (500+offset[0], 500+offset[1])
        robot_pos = (594+offset[0], 522+offset[1])
        self.test_tower.place(tower_pos)
        self.test_robot.rect.center = robot_pos

        # There should be no projectiles
        self.assertEqual(len(self.test_game.get_projectiles()), 0)

        # Does tower shoot at robot?
        pygame.time.wait(1000)
        self.test_game.update()
        self.assertEqual(len(self.test_game.get_projectiles()), 1)
