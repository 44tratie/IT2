import pygame as pg
from classes.direction import Direction
from custom_types import RGBTuple

from .object import Object


class Troll(Object):
    """Represents the Troll in PacTroll, the playable character."""

    COLOR: RGBTuple = (0, 255, 0)

    def __init__(self, x: int, y: int, window: pg.Surface) -> None:
        super().__init__(x, y, self.COLOR, window)

        self.velocity = 3
        self.acceration = 0.5

        # used to keep track of key-press order
        self._direction_stack = []
        self._last_direction = Direction.UP  # default direction when game starts

    @property
    def direction(self) -> Direction:
        """The current direction, giving priority to most recently pressed keys."""
        if not self._direction_stack:
            return self._last_direction

        self._last_direction = self._direction_stack[-1]

        return self._last_direction

    def move(self) -> None:
        """Moves the player in the current direction."""
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

    def accelerate(self) -> None:
        """Increases the velocity of the Troll."""
        self.velocity += self.acceration

    def add_direction(self, direction: Direction) -> None:
        """Adds a direction to the direction stack."""
        self._direction_stack.append(direction)

    def remove_direction(self, direction: Direction) -> None:
        """Removes a direction from the direction stack."""
        self._direction_stack.remove(direction)

    def is_in_bounds(self) -> bool:
        """Helper-function to check if the Troll is within the bounds."""
        # if x in interval and y in interval, then troll is within playing field
        return (
            0 <= self.x <= self.window.get_width() - self.WIDTH
            and 0 <= self.y <= self.window.get_height() - self.HEIGHT
        )
