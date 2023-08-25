""" src/game/player.py """
from utils.logger import logger


class Player:
    """"
        This class represents the player of the game.
        It has properties such as money and lives,
        and methods for earning and spending money,
        as well as for losing lives.

        Attributes:
            money (int): The amount of money the player has.
            health (int): The amount of health the player has.
            lost (bool): Whether the player has lost the game or not.
    """

    def __init__(self, money: int = 250) -> None:
        self.__starting_money = money
        self.__money = money
        self.__health = 100
        self.__alive = True

    def spend_money(self, amount) -> None:
        if self.__money >= amount:
            self.__money -= amount

    def earn_money(self, amount) -> None:
        self.__money += amount
        logger.debug(f"Player ({id(self)}) new money: {self.__money} $")

    def lose_health(self, amount) -> None:
        if self.__health >= amount:
            self.__health -= amount
        if self.__health <= 0:
            self.__alive = False
        logger.debug(f"Player ({id(self)}) new health: {self.__health} HP")

    def reset(self) -> None:
        self.__health = 100
        self.__money = self.__starting_money
        self.__alive = True

    @property
    def health(self):
        return self.__health

    @property
    def money(self):
        return self.__money

    @property
    def alive(self):
        return self.__alive
