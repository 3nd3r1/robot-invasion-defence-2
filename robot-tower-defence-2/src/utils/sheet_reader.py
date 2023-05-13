import pygame
from utils.file_reader import get_image


def get_sheet_images(sheet_file, sheet_size) -> list:
    sheet_image = pygame.image.load(
        get_image(sheet_file)).convert_alpha()
    tile_size = (sheet_image.get_width() //
                 sheet_size[0], sheet_image.get_height()//sheet_size[1])

    images = []
    rects = []

    for i in range(0, sheet_image.get_height(), tile_size[1]):
        for j in range(0, sheet_image.get_width(), tile_size[0]):
            rects.append(pygame.Rect((j, i), tile_size))

    for rect in rects:
        images.append(sheet_image.subsurface(rect))

    return images
