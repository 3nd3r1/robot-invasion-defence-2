""" src/game/map.py """
import pytmx
import pygame
from utils.config import arenas
from utils.file_reader import get_tmx


class Map:
    """
      This class represents the map on which the game is played.
      It has methods for loading and displaying the map.
    """

    def __init__(self, arena: str, offsetx: int, offsety: int) -> None:

        self.__tmx = pytmx.load_pygame(
            get_tmx(arenas[arena]["map_file"]))

        self.__width = self.__tmx.width * self.__tmx.tilewidth
        self.__height = self.__tmx.height * self.__tmx.tileheight
        self.__map = pygame.Surface((self.__width, self.__height))

        self.__screen_offsetx = offsetx
        self.__screen_offsety = offsety

        self.__obstacles = []
        self.__path = []
        self.__water = []
        self.__waypoints = []

        self.__render_map()

    def __render_map(self) -> None:
        """ Renders an image of the map """
        tw = self.__tmx.tilewidth
        th = self.__tmx.tileheight
        for layer in self.__tmx.visible_layers:
            # Load waypoints
            if layer.name == "waypoints":
                for waypoint in layer:
                    self.__waypoints.append(
                        self.__to_screen_coords(waypoint.x, waypoint.y))
                continue

            # Load obstacles, water and path and draw them to the map
            for x, y, gid in layer:
                tile = self.__tmx.get_tile_image_by_gid(gid)
                if tile:
                    self.__map.blit(tile, (x*th, y*tw))
                    if layer.name == "obstacles" or layer.name == "obstacles2":
                        self.__obstacles.append(
                            pygame.Rect(self.__to_screen_coords(x*tw, y*th), (tw, th)))
                    if layer.name == "water":
                        self.__water.append(pygame.Rect(
                            self.__to_screen_coords(x*tw, y*th), (tw, th)))
                    if layer.name == "path":
                        self.__path.append(pygame.Rect(
                            self.__to_screen_coords(x*tw, y*th), (tw, th)))

    def get_waypoints(self) -> list:
        """ Returns a list of waypoints """
        return self.__waypoints

    def is_valid_tower_position(self, tower: "Tower") -> bool:
        """ Checks if a rectangle is a valid position for a tower """
        # Check if the rectangle is in an obstacle
        if self.__is_in_obstacle(tower.rect):
            return False

        # Check if the rectangle is in water
        if self.__is_in_water(tower.rect) and not tower.can_be_in_water():
            return False

        # Check if the rectangle is in the path
        if self.__is_in_path(tower.rect):
            return False

        # Check if the rectangle is in the map
        if not self.__is_in_map(tower.rect):
            return False

        return True

    def __is_in_obstacle(self, rect: pygame.Rect) -> bool:
        """ Checks if a rectangle is in an obstacle """
        for obstacle in self.__obstacles:
            if obstacle.collidepoint(rect.center):
                return True
        return False

    def __is_in_water(self, rect: pygame.Rect) -> bool:
        """ Checks if a rectangle is in water """
        for water in self.__water:
            if water.collidepoint(rect.center):
                return True
        return False

    def __is_in_path(self, rect: pygame.Rect) -> bool:
        """ Checks if a rectangle is in the path """
        for path in self.__path:
            if path.collidepoint(rect.center):
                return True
        return False

    def __is_in_map(self, rect: pygame.Rect) -> bool:
        """ Checks if a rectangle is in the map """
        return self.__screen_offsetx < rect.centerx < self.__width+self.__screen_offsetx and self.__screen_offsety < rect.centery < self.__height+self.__screen_offsety

    def __to_screen_coords(self, x: int, y: int) -> tuple:
        """ Converts map coordinates to screen coordinates """
        return (x + self.__screen_offsetx, y + self.__screen_offsety)

    def draw(self, screen) -> None:
        """ Draws the image of the map to the main surface """
        screen.blit(self.__map, (self.__screen_offsetx, self.__screen_offsety))
