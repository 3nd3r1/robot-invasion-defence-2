""" src/game/map.py """
import pytmx
import pygame
from utils.config import arenas
from utils.file_reader import get_tmx


class Map():
    """
      This class represents the map on which the game is played.
      It has methods for loading and displaying the map.
    """

    def __init__(self, arena, offset):

        self.__tmx = pytmx.load_pygame(
            get_tmx(arenas[arena]["map_file"]))

        self.__width = self.__tmx.width * self.__tmx.tilewidth
        self.__height = self.__tmx.height * self.__tmx.tileheight

        self.__map_img = pygame.Surface((self.__width, self.__height))
        self.__offset = offset

        self.__obstacles = []
        self.__path = []
        self.__water = []
        self.__waypoints = []

        self.__render_map()

    def __render_map(self):
        """ Renders an image of the map """
        tile_width = self.__tmx.tilewidth
        tile_height = self.__tmx.tileheight

        for layer in self.__tmx.visible_layers:
            # Load waypoints
            if layer.name == "waypoints":
                for waypoint in layer:
                    self.__waypoints.append(
                        self.__to_screen_coords((waypoint.x, waypoint.y)))
                continue

            # Load obstacles, water and path and draw them to the map
            for image_x, image_y, gid in layer:
                tile = self.__tmx.get_tile_image_by_gid(gid)
                if tile:
                    tile_coords = (image_x*tile_width, image_y*tile_height)
                    self.__map_img.blit(tile, tile_coords)
                    if layer.name in ("obstacles", "obstacles2"):
                        self.__obstacles.append(pygame.Rect(
                            self.__to_screen_coords(tile_coords), (tile_width, tile_height)))
                    if layer.name == "water":
                        self.__water.append(pygame.Rect(
                            self.__to_screen_coords(tile_coords), (tile_width, tile_height)))
                    if layer.name == "path":
                        self.__path.append(pygame.Rect(
                            self.__to_screen_coords(tile_coords), (tile_width, tile_height)))

    def get_waypoints(self) -> list:
        """ Returns a list of waypoints """
        return self.__waypoints

    def is_in_obstacle(self, rect) -> bool:
        """ Checks if a rectangle is in an obstacle """
        for obstacle in self.__obstacles:
            if obstacle.colliderect(rect):
                return True
        return False

    def is_in_water(self, rect) -> bool:
        """ Checks if a rectangle is in water """
        for water in self.__water:
            if water.collidepoint(rect.center):
                return True
        return False

    def is_in_path(self, rect) -> bool:
        """ Checks if a rectangle is in the path """
        for path in self.__path:
            if path.collidepoint(rect.center):
                return True
        return False

    def is_in_map(self, rect) -> bool:
        """ Checks if a rectangle is in the map """
        is_in_x = self.get_offset()[0] < rect.centerx < self.__width+self.get_offset()[0]
        is_in_y = self.get_offset()[1] < rect.centery < self.__height+self.get_offset()[1]

        return is_in_x and is_in_y

    def __to_screen_coords(self, coords) -> tuple:
        """ Converts map coordinates to screen coordinates """
        return (coords[0] + self.get_offset()[0], coords[1] + self.get_offset()[1])

    def draw(self, screen):
        """ Draws the image of the map to the main surface """
        screen.blit(self.__map_img, self.get_offset())

    def get_offset(self) -> tuple:
        """ Returns the map offset """
        return self.__offset
