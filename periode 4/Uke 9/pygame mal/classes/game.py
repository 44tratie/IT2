import pygame as pg

from settings import GAME_FPS, WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    """Represents a game of ___ and is meant to be the entry point."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("___")

        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True

    def run(self) -> None:
        """Acts as the entry point for the game."""
        self.clock = pg.time.Clock()

        while self.running:
            # handles input-related events
            self._handle_events()

            # colors the background black
            self.window.fill((0, 0, 0))

            # handles in-game events / ruleset
            self._handle_game_events()

            # draws labels
            self._draw_labels()

            # updates the content in the window
            self._update_frame()

        # freeze the game after game is ended
        self._display_end_screen()

    def _handle_events(self) -> None:
        """Handles pygame events"""
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.running = False

    def _handle_game_events(self) -> None:
        """Handles in-game events"""
        pass

    def _draw_labels(self) -> None:
        """Draws the labels in the game."""
        pass

    def _update_frame(self) -> None:
        """Updates frame so the user can see change."""
        pg.display.flip()
        self.clock.tick(GAME_FPS)

    def _display_end_screen(self) -> None:
        """Displays a loss screen after the game is ended."""
        while True:
            # checks for exits
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            # updates the content in the window
            self._update_frame()
