import pygame as pg
import random

from settings import GEN_0_ALIVE_CHANCE

class Cell:
    """Represents a cell in the Game of Life"""

    COLOR = "black"
    SIZE = 25

    def __init__(self, window: pg.Surface, x: int, y: int, initial_state: bool = None) -> None:
        self.window = window
        self.x = x
        self.y = y

        self.is_alive = initial_state

        if initial_state is None:
            self.is_alive = random.random() < GEN_0_ALIVE_CHANCE

    
    @property
    def row_i(self) -> int:
        """The row index of the cell in the grid"""
        return self.y // Cell.SIZE
    
    @property
    def col_i(self) -> int:
        """The col index of the cell in the grid"""
        return self.x // Cell.SIZE


    def draw(self) -> None:
        """Draw the cell according to game rules (if it is alive)"""
        if self.is_alive:
            pg.draw.rect(self.window, Cell.COLOR, (self.x, self.y, Cell.SIZE, Cell.SIZE))