""" src/game/towers/turret.py """
from game.tower import Tower


class Turret(Tower):
    """ Turret tower class """

    def __init__(self) -> None:
        super().__init__()
        self.tower_name = "turret"
        self.load_image()

    def load_image(self) -> None:
        super().load_image(self.tower_name)

    def shoot(self) -> None:
        """ Shoots a turret projectile """
        pass
