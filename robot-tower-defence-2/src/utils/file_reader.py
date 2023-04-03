""" src/utils/file_reader.py """
import os
import __main__

main_dir = os.path.dirname(__main__.__file__)
resources_dir = os.path.join(main_dir, "resources")
arenas_dir = os.path.join(resources_dir, "arenas")
images_dir = os.path.join(resources_dir, "images")


def get_image(file: str) -> str:
    return os.path.join(images_dir, file)


def get_tmx(file: str) -> str:
    return os.path.join(arenas_dir, file)
