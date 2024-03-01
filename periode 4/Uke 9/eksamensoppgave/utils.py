import pygame as pg
from settings import WINDOW_HEIGHT, WINDOW_WIDTH


def init_game_window() -> pg.Surface:
    # Initialiserer/starter pygame
    pg.init()

    # Oppretter et vindu der vi skal "tegne" innholdet vårt
    window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    return window
