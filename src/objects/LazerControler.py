import pygame

from ..options import *
from ..assets import *

class LazerControler:
    instance = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (100, 50)
        self.image = pygame.transform.scale(LAZER_CONTROLER_IMAGE, self.size)
        self.done = False

        LazerControler.instance = self

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def can_interact(self, px, py, p_size):
        is_close = (self.x < px+p_size[0] and self.y < py+p_size[1] and self.x+self.size[0] > px and self.y+self.size[1] > py)
        return is_close and not self.done
