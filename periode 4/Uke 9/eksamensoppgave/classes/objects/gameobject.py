from __future__ import annotations

import pygame as pg

from settings import OBJECT_SIZE
from custom_types import RGBTuple


class GameObject:
    """Represents a generic square object in PacTroll."""

    WIDTH: float = OBJECT_SIZE
    HEIGHT: float = OBJECT_SIZE

    def __init__(self, x: int, y: int, color: RGBTuple, window: pg.Surface) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.window = window

    def draw(self) -> None:
        """Draws the object"""
        pg.draw.rect(self.window, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def overlaps_with(self, other: GameObject) -> bool:
        """Helper-function to check for overlaps with another object."""
        # assumes other is stationary and checks whether
        # a corner of self is within the others perimeter

        # checks for overlap on the left-side
        if other.x <= self.x <= other.x + other.WIDTH:
            # checks overlap in the top-left corner
            if other.y <= self.y <= other.y + other.HEIGHT:
                return True
            # checks overlap in the bottom-left corner
            elif other.y <= self.y + self.HEIGHT <= other.y + other.HEIGHT:
                return True
        # checks for overlap on the right-side
        elif other.x <= self.x + self.HEIGHT <= other.x + other.WIDTH:
            # checks overlap in the top-right corner
            if other.y <= self.y <= other.y + other.HEIGHT:
                return True
            # checks overlap in the bottom-right corner
            elif other.y <= self.y + self.HEIGHT <= other.y + other.HEIGHT:
                return True

        # if this point is reached then no corners overlap
        return False
