from enum import Enum, unique

from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP


@unique
class Direction(Enum):
    """Maps pygame-keys as enum-values to player directions"""

    LEFT = K_LEFT
    RIGHT = K_RIGHT
    UP = K_UP
    DOWN = K_DOWN


KEY_VALUES = set((K_LEFT, K_RIGHT, K_UP, K_DOWN))
