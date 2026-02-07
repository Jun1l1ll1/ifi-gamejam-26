import pygame

from ..options import *
from ..assets import *

class VirusGrowthOverlay:
    def __init__(self, max_alpha = 255):
        self._max_alpha = max_alpha
        self.alpha = 0

    def draw(self, screen):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(self.alpha)
        overlay.fill(PURPLE)
        screen.blit(overlay, (0, 0))

    def increse_alpha(self, growth):
        self.alpha = growth/VIRUS_GROWTH_KILL * self._max_alpha
