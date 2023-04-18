from utils.config import general


class Logger:
    def __init__(self, debug: bool) -> None:
        self.__debug = debug

    def debug(self, message: str) -> None:
        if self.__debug:
            print(f"[DEBUG]: {message}")

    def error(self, message: str) -> None:
        print(f"[ERROR]: {message}")

    def info(self, message: str) -> None:
        print(f"[INFO]: {message}")


logger = Logger(general["debug"])
