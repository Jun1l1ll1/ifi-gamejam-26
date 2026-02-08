import pygame

from ..options import *
from ..assets import *

class GingerPlant:
    all = []

    def __init__(self, x, y, room = GROWTH_ROOM_NAME):
        self.x = x
        self.y = y
        self.size = (200, 100)
        self.image = pygame.transform.scale(GINGER_PLANT_SMAL_IMAGE, self.size)
        self.empty = False
        self.grown = False

        GingerPlant.all.append((self, room))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def grow(self):
        if not self.grown and not self.empty:
            self.image = pygame.transform.scale(GINGER_PLANT_BIG_IMAGE, self.size)
            self.grown = True

    def can_take(self, px, py, p_size):
        is_close = (self.x < px+p_size[0] and self.y < py+p_size[1] and self.x+self.size[0] > px and self.y+self.size[1] > py)
        return is_close and self.grown and not self.empty
    
    def take(self):
        if not self.empty:
            self.image = pygame.transform.scale(GINGER_PLANT_EMPTY_IMAGE, self.size)
            self.empty = True
            return GINGER
        return ""

