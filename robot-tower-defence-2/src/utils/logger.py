from utils.config import DEBUG


class Logger:
    def __init__(self, debug: bool) -> None:
        self.__debug = debug

    def debug(self, message: str) -> None:
        if self.__debug:
            print("[DEBUG]: {}".format(message))

    def error(self, message: str) -> None:
        print("[ERROR]: {}".format(message))

    def info(self, message: str) -> None:
        print("[INFO]: {}".format(message))


logger = Logger(DEBUG)
