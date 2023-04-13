import pygame
from utils.config import robots
from utils.file_reader import get_image


def get_robot_walk_images(robot_name: str) -> list:
    sheet = pygame.image.load(
        get_image(robots[robot_name]["walk_sheet"])).convert_alpha()
    sheet_size = robots[robot_name]["walk_sheet_size"]
    tile_size = (sheet.get_width() //
                 sheet_size[0], sheet.get_height()//sheet_size[1])

    images = []
    rects = []

    for i in range(0, sheet.get_height(), tile_size[1]):
        for j in range(0, sheet.get_width(), tile_size[0]):
            rects.append(pygame.Rect((j, i), tile_size))

    for rect in rects:
        images.append(sheet.subsurface(rect))

    return images
