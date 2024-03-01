import random

import pygame as pg
from custom_types import RGBTuple
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

from .object import Object


class Food(Object):
    COLOR: RGBTuple = (255, 255, 0)

    def __init__(self, window: pg.Surface) -> None:
        super().__init__(
            random.randint(0, WINDOW_WIDTH - self.WIDTH),
            random.randint(0, WINDOW_HEIGHT - self.HEIGHT),
            self.COLOR,
            window,
        )
