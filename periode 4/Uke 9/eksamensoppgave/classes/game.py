import random

import pygame as pg
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

from .direction import KEY_VALUES, Direction
from .objects import Food, Object, Obstacle, Troll


class Game:
    """Represents a game of PacTroll and is meant to be the entry point."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("PacTroll")

        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True

        self.score = 0

        self.player = Troll(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, self.window)
        self.obstacles = []

        self.food_objects = [Food(self.window)]
        self._add_food_object()
        self._add_food_object()

    @property
    def objects(self) -> list[Object]:
        """All current objects in the game"""
        return [self.player] + self.obstacles + self.food_objects

    def _add_food_object(self) -> None:
        """Adds a food-object to the game."""
        # this process ensures non-overlaps, but can be slow as it's brute force
        new_food = Food(self.window)
        while not all((not new_food.overlaps_with(other) for other in self.objects)):
            new_food = Food(self.window)

        self.food_objects.append(new_food)

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
        self._display_loss()

    def _handle_events(self) -> None:
        """Handles pygame events"""
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.running = False
                case pg.KEYDOWN:
                    if event.key in KEY_VALUES:
                        self.player.add_direction(Direction(event.key))
                case pg.KEYUP:
                    if event.key in KEY_VALUES:
                        self.player.remove_direction(Direction(event.key))

    def _handle_game_events(self) -> None:
        """Handles in-game events"""
        # moves and draws the player
        self.player.move()
        self.player.draw()

        # checks for collisions
        for object in self.objects:
            if object == self.player:
                continue

            # check and handle overlaps
            self._check_overlap(object)

            # object has been handled means it's safe to draw
            object.draw()

        # checks if player is within bounds
        if not self.player.is_in_bounds():
            self.running = False

    def _check_overlap(self, object) -> None:
        """Checks if the player overlaps with an object, and handles the cases."""
        if self.player.overlaps_with(object):
            self._handle_overlap(object)

        # set new obstacles to kill on next overlap
        elif isinstance(object, Obstacle):
            if not object.can_kill:
                object.can_kill = True

    def _handle_overlap(self, object) -> None:
        """Handles overlaps."""
        match object:
            case Food():
                self.obstacles.append(Obstacle(object.x, object.y, self.window))
                self.food_objects.remove(object)
                self._add_food_object()
                self.player.accelerate()
                self.score += 1
            case Obstacle():
                if object.can_kill:
                    self.running = False

    def _draw_labels(self) -> None:
        """Draws score label on the top-right corner."""
        score_label = pg.font.SysFont("calibri", self.window.get_height() // 10).render(
            f"Score: {self.score}", True, (255, 255, 255)
        )
        score_label_rect = score_label.get_rect()
        score_label_rect.topleft = (10, 10)

        self.window.blit(score_label, score_label_rect)

    def _update_frame(self) -> None:
        """Updates frame so the user can see change."""
        pg.display.flip()
        self.clock.tick(30)

    def _display_loss(self) -> None:
        """Displays a loss screen after the game is ended."""
        while True:
            # checks for exits
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            # adds a loss label
            loss_label = pg.font.SysFont(
                "calibri", self.window.get_height() // 5
            ).render(f"Game Over", True, (255, 255, 255))
            loss_label_rect = loss_label.get_rect()
            loss_label_rect.center = (
                self.window.get_width() // 2,
                self.window.get_height() // 2,
            )

            self.window.blit(loss_label, loss_label_rect)

            # updates the content in the window
            self._update_frame()
