
import pygame as pg

from pygame.locals import K_SPACE, K_ESCAPE, K_DELETE

from settings import GAME_FPS, TIME_PER_GENERATION, WINDOW_HEIGHT, WINDOW_WIDTH
from .grid import Grid
from .cell import Cell

class Game:
    """Represents a game of Game of Life and is meant to be the entry point."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Game of Life")

        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        gen_0_cells = [[Cell(self.window, x, y) for x in range(0, WINDOW_WIDTH, Cell.SIZE)] for y in range(0, WINDOW_HEIGHT, Cell.SIZE)]
        self.grid = Grid(self.window, gen_0_cells)
        
        self.running = True
        self.time_since_last_generation = 0
        
        self.paused = False

    def run(self) -> None:
        """Acts as the entry point for the game."""
        self.clock = pg.time.Clock()

        while self.running:
            # handles input-related events
            self._handle_events()

            # colors the background black
            self.window.fill("white")

            self.grid.draw()

            # handles in-game events / ruleset
            self._handle_game_events()

            # updates the content in the window
            self._update_frame()

    def _handle_events(self) -> None:
        """Handles pygame events"""
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.running = False
                case pg.KEYUP:
                    if event.key == K_SPACE:
                        self.grid.calculate_next_generation()
                    elif event.key == K_DELETE:
                        self.grid.nullify()
                    elif event.key == K_ESCAPE:
                        self.paused = not self.paused
                case pg.MOUSEBUTTONDOWN:
                    self.grid.invert_cell(pg.mouse.get_pos())

    def _handle_game_events(self) -> None:
        """Handles in-game events"""

        if self.time_since_last_generation > TIME_PER_GENERATION:
            self.grid.calculate_next_generation()
            self.time_since_last_generation = 0

    def _update_frame(self) -> None:
        """Updates frame so the user can see change."""
        pg.display.flip()
        delta_time = self.clock.tick(GAME_FPS)

        if not self.paused:
            self.time_since_last_generation += delta_time