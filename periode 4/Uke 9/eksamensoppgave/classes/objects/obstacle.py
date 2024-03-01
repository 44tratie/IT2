import pygame as pg
from custom_types import RGBTuple

from .object import Object


class Obstacle(Object):
    WIDTH = 40
    HEIGHT = 40
    COLOR: RGBTuple = (128, 128, 128)

    def __init__(self, x: int, y: int, window: pg.Surface) -> None:
        super().__init__(x, y, self.COLOR, window)

        self.can_kill = False
