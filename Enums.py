# Description: Holds all game enumerations
# Author: Jacob Maughan

# Sys Imports
from enum import Enum

class GameState(Enum):
    GAME = 1
    MAP_EDITOR = 99

class PlayerState(Enum):
    IDLE = 1
    WALKING = 2

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4