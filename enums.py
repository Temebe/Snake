from enum import Enum

mapSize = 20
squareSize = 20
gapSize = 5

class SquareType(Enum):
    BODY = 0
    FRUIT = 1
    BACKGROUND = 2

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3