from game.ui.hud import Hud

class Ui:
    """ This class represents the user interface of the game. It has methods for displaying information about the game, such as the player's score and the number of lives remaining. """

    def __init__(self) -> None:
        self.__hud = Hud()

    def draw(self, surface) -> None:
        """ Draws all components to the screen """
        self.__hud.draw(surface)
