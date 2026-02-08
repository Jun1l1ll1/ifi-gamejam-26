import pygame

from .options import *
from .assets import *

class SafeHint:
    instance = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.text = FONT_TYPE.render("Safe: 3 - 1 - 5 - 2 - 4", False, BLACK)

        SafeHint.instance = self

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))
