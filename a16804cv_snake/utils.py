from enum import Enum


class COLOR(Enum):

    RED = 0
    GREEN = 1
    OTHER = 3


class COLOR_BOUNDARY(Enum):
    RED_LOWER_BOUNDARY = (0, 0, 150)
    RED_UPPER_BOUNDARY = (100, 100, 255)

    GREEN_LOWER_BOUNDARY = (45, 0, 0)
    GREEN_UPPER_BOUNDARY = (90, 255, 250)

    MAX_BOUNDARY = (255, 255, 255)


class DIRECTION(Enum):

    LEFT = 0
    RIGHT = 1
    OTHER = 2
