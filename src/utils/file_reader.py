""" src/utils/file_reader.py """
import os
from pathlib import Path

main_dir = Path(__file__).parents[1]
resources_dir = os.path.join(main_dir, "resources")
arenas_dir = os.path.join(resources_dir, "arenas")
images_dir = os.path.join(resources_dir, "images")
fonts_dir = os.path.join(resources_dir, "fonts")
data_dir = os.path.join(main_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)


def get_image(file: str) -> str:
    return os.path.join(images_dir, file)


def get_tmx(file: str) -> str:
    return os.path.join(arenas_dir, file)


def get_font(file: str) -> str:
    return os.path.join(fonts_dir, file)


def get_database(file: str) -> str:
    return os.path.join(data_dir, file)


def get_env(file: str) -> str:
    return os.path.join(main_dir, file)
