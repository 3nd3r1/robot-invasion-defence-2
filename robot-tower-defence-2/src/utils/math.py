import math


def distance_between_points(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def get_angle(x, y):
    return math.degrees(math.atan2(y, x))
