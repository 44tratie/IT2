import pygame as pg
from custom_types import RGBTuple

from .gameobject import GameObject


class Obstacle(GameObject):
    """Represents an obstacle in PacTroll. Players die when these are hit "the second time"."""

    COLOR: RGBTuple = (128, 128, 128)

    def __init__(self, x: int, y: int, window: pg.Surface) -> None:
        super().__init__(x, y, self.COLOR, window)

        # since obstacles come from food-objects,
        # the first overlap should not kill
        self.can_kill = False
