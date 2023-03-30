class Robot:
    """This class represents a robot that moves along the map. It has properties such as speed, health, and type, and methods for moving and being damaged."""

    def __init__(self, health: int, spawnLocation: tuple) -> None:
        self.__health = health
        self.__location = spawnLocation
