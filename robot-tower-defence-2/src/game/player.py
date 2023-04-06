class Player:
    """" This class represents the player of the game. It has properties such as money and lives, and methods for earning and spending money, as well as for losing lives. """

    def __init__(self) -> None:
        self.__money = 0
        self.__health = 100
        self.lost = False

    def get_money(self) -> int:
        return self.__money

    def spend_money(self, amount) -> None:
        if self.__money >= amount:
            self.__money -= amount

    def get_health(self) -> int:
        return self.__health

    def lose_health(self, amount) -> None:
        if self.__health >= amount:
            self.__health -= amount
        if self.__health <= 0:
            self.lost = True
