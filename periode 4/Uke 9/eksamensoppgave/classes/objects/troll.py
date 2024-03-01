import pygame as pg
from classes.direction import Direction
from custom_types import RGBTuple

from .object import Object


class Troll(Object):
    COLOR: RGBTuple = (0, 255, 0)

    def __init__(self, x: int, y: int, window: pg.Surface) -> None:
        super().__init__(x, y, self.COLOR, window)

        self.velocity = 5
        self._direction_stack = []
        self._last_direction = Direction.UP

    @property
    def direction(self) -> Direction:
        if not self._direction_stack:
            return self._last_direction

        self._last_direction = self._direction_stack[-1]

        return self._last_direction

    def move(self) -> None:
        # y is flipped in pygame, so up = -y
        match self.direction:
            case Direction.UP:
                self.y -= self.velocity
            case Direction.DOWN:
                self.y += self.velocity
            case Direction.LEFT:
                self.x -= self.velocity
            case Direction.RIGHT:
                self.x += self.velocity

    def add_direction(self, direction: Direction) -> None:
        self._direction_stack.append(direction)

    def remove_direction(self, direction: Direction) -> None:
        self._direction_stack.remove(direction)
