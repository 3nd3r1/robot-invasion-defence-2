import inspect
from utils.config import general


class Logger:
    def __init__(self, debug: bool) -> None:
        self.__debug = debug

    def debug(self, message: str) -> None:
        filename = inspect.stack()[1].filename.split("\\")[-1]
        if self.__debug:
            print(f"[DEBUG] ({filename}): {message}")

    def error(self, message: str) -> None:
        print(f"[ERROR]: {message}")

    def info(self, message: str) -> None:
        print(f"[INFO]: {message}")


logger = Logger(general["debug"])
