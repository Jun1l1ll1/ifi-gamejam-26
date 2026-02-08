import pygame

from ..options import *
from ..assets import *

class Safe:
    all = []

    def __init__(self, x, y, content = TOOTH_PASTE, room = BATH_ROOM_NAME):
        self.x = x
        self.y = y
        self.size = (70, 70)
        self.image = pygame.transform.scale(SAFE_LOCKED_IMAGE, self.size)
        self.locked = True
        self.empty = False
        self.content = content

        Safe.all.append((self, room))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def can_take(self, px, py, p_size):
        is_close = (self.x < px+p_size[0] and self.y < py+p_size[1] and self.x+self.size[0] > px and self.y+self.size[1] > py)
        return is_close and not self.locked
    
    def open(self):
        self.locked = False
        self.image = pygame.transform.scale(SAFE_OPEN_IMAGE, self.size)

    def take_content(self):
        c = self.content
        self.content = "" # Remove content
        return c

