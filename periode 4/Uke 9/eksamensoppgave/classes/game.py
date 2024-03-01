import random

import pygame as pg
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

from .direction import KEY_VALUES, Direction
from .objects import Food, Object, Obstacle, Troll


class Game:
    def __init__(self) -> None:
        pg.init()

        self.window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True

        self.player = Troll(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, self.window)
        self.obstacles = []

        self.food_objects = [Food(self.window)]
        self._add_food_object()
        self._add_food_object()

    @property
    def objects(self) -> list[Object]:
        return [self.player] + self.obstacles + self.food_objects

    def _add_food_object(self) -> None:
        new_food = Food(self.window)
        while not all((not new_food.overlaps_with(other) for other in self.objects)):
            new_food = Food(self.window)

        self.food_objects.append(new_food)

    def run(self) -> None:
        self.clock = pg.time.Clock()

        while self.running:
            # handles input-related events
            self._handle_events()

            # colors the background black
            self.window.fill((0, 0, 0))

            # handles in-game events / ruleset
            self._handle_game_events()

            # updates the content in the window
            self._update_frame()

        pg.quit()

    def _handle_events(self) -> None:
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
        # moves and draws the player
        self.player.move()
        # self.player.draw()

        self.test = Object(490, 490, (128, 128, 128), self.window)
        self.test.draw()
        # checks for collisions

        for object in self.objects:
            if object == self.player:
                continue

            if self.player.overlaps_with(object):
                match object:
                    case Food():
                        self.obstacles.append(Obstacle(object.x, object.y, self.window))
                        self.food_objects.remove(object)
                        self._add_food_object()
                    case Obstacle():
                        if object.can_kill:
                            print("noob")
            else:
                match object:
                    case Obstacle():
                        if object.can_kill == False:
                            object.can_kill = True

        for object in self.objects:
            object.draw()

    def _update_frame(self) -> None:
        pg.display.flip()
        self.clock.tick(30)
