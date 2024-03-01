import random

import pygame as pg
from custom_types import RGBTuple

from .object import Object


class Food(Object):
    """Represents a Food-object in PacTroll. Players gain points by collecting these."""

    COLOR: RGBTuple = (255, 255, 0)

    def __init__(self, window: pg.Surface) -> None:
        super().__init__(
            random.randint(0, window.get_width() - self.WIDTH),
            random.randint(0, window.get_height() - self.HEIGHT),
            self.COLOR,
            window,
        )
