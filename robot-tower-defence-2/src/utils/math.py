import math


def distance_between_points(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)


def get_angle(coord_x, coord_y):
    return math.degrees(math.atan2(coord_y, coord_x))
