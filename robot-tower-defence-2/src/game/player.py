class Player:
    """" This class represents the player of the game. It has properties such as money and lives, and methods for earning and spending money, as well as for losing lives. """

    def __init__(self) -> None:
        self.__money = 0
        self.__hp = 100
        self.lost = False

    def getMoney(self) -> int:
        return self.__money

    def spendMoney(self, amount) -> None:
        if self.__money >= amount:
            self.__money -= amount

    def getHp(self) -> int:
        return self.__hp

    def loseHp(self, amount) -> None:
        if self.__hp >= amount:
            self.__hp -= amount
        if self.__hp <= 0:
            self.lost = True
