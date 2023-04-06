import pygame
from utils.config import robots
from utils.file_reader import get_image


def get_robot_walk_images(robot_name: str) -> list:
    sheet = pygame.image.load(
        get_image(robots[robot_name]["walk_sheet"])).convert_alpha()
    images = []
    for rect in robots[robot_name]["walk_rects"]:
        images.append(sheet.subsurface(rect))
    return images
