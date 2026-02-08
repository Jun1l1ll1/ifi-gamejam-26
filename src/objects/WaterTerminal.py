import pygame

from ..options import *
from ..assets import *

class WaterTerminal:
    instance = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (200, 100)
        self.image = pygame.transform.scale(WATERING_TERMINAL_INACTIVE_IMAGE, self.size)
        self.active = False

        WaterTerminal.instance = self

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def can_interact(self, px, py, p_size):
        is_close = (self.x < px+p_size[0] and self.y < py+p_size[1] and self.x+self.size[0] > px and self.y+self.size[1] > py)
        return is_close and not self.active

    def activate(self):
        self.active = True
        self.image = pygame.transform.scale(WATERING_TERMINAL_ACTIVE_IMAGE, self.size)
