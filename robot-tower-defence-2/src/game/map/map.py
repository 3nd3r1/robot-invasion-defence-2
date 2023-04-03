""" File containing Map Class """
import os
import pytmx
import pygame
import __main__
from game.arenas.arenas import arenas


class Map:
    """
      This class represents the map on which the game is played.
      It has methods for loading and displaying the map. 
    """

    def __init__(self, arena: str) -> None:
        main_folder = os.path.dirname(__main__.__file__)
        arena_folder = os.path.join(main_folder, "data/arenas")

        self.__tmx = pytmx.load_pygame(os.path.join(
            arena_folder, arenas[arena]["map_file"]))

        self.__width = self.__tmx.width * self.__tmx.tilewidth
        self.__height = self.__tmx.height * self.__tmx.tileheight
        self.__map = pygame.Surface((self.__width, self.__height))
        self.__obstacles = []
        self.__water = []

        self.render_map()

    def render_map(self) -> None:
        """ Renders an image of the map """
        tw = self.__tmx.tilewidth
        th = self.__tmx.tileheight
        for layer in self.__tmx.visible_layers:
            for x, y, gid in layer:
                tile = self.__tmx.get_tile_image_by_gid(gid)
                if tile:
                    self.__map.blit(tile, (x*th, y*tw))
                    if layer.name == "obstacles" or layer.name == "obstacles2":
                        self.__obstacles.append(
                            pygame.Rect(x*tw, y*th, tw, th))
                    if layer.name == "water":
                        self.__water.append(pygame.Rect(x*tw, y*th, tw, th))

    def draw(self, surface) -> None:
        """ Draws the image of the map to the main surface """
        surface.blit(self.__map)
