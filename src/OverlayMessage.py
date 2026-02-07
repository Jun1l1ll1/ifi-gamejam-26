import pygame

from .options import *
from .assets import *

class OverlayMessage:
    def __init__(self, text, w):
        self.w = w
        self.h = 70
        self.show = False
        self.x = (WIDTH - self.w)/2
        self.y = (HEIGHT - self.h)/2
        self.text = FONT_TYPE.render(text, False, FONT_COLOR)

    def draw(self, screen):
        background = pygame.Surface((WIDTH, self.h))
        background.set_alpha(175) # Make background transparent
        screen.blit(background, (0, self.y))
        screen.blit(self.text, (self.x, self.y+20))
