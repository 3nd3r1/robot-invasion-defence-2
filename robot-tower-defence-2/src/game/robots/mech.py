from game.robot import Robot
from utils.sheet_reader import get_robot_walk_images
from utils.config import robots


class Mech(Robot):
    def __init__(self, health: int, game: "Game") -> None:
        super().__init__(health, game)
        self._speed = robots["mech"]["speed"]
        self._damage = robots["mech"]["damage"]
        self.__load_walking()

    def __load_walking(self):
        self._walking_images = get_robot_walk_images("mech")
        self._walking_frame = 0
        self._animation_timer = robots["mech"]["animation_interval"]
        self._animation_interval = robots["mech"]["animation_interval"]
