import pygame
import math
from ..options import *

class VirusGrowthOverlay:
    def __init__(self, max_alpha=220):
        self.max_alpha = max_alpha
        self.alpha = 0

        # Pre-render vignette surface once (performance-friendly)
        self.vignette = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self._create_vignette()

    def _create_vignette(self):
        """Create a radial vignette mask"""
        center_x, center_y = WIDTH // 2, HEIGHT // 2
        max_radius = math.hypot(center_x, center_y)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                dist = math.hypot(x - center_x, y - center_y)
                strength = min(dist / max_radius, 1)
                alpha = int(strength * 255)
                self.vignette.set_at((x, y), (200, 40, 90, alpha))


    def draw(self, screen):
        # Control intensity via alpha
        overlay = self.vignette.copy()
        overlay.set_alpha(self.alpha)
        screen.blit(overlay, (0, 0))

    def increse_alpha(self, growth):
        # Virus growth controls how much the vignette closes in
        self.alpha = min(
            int((growth / VIRUS_GROWTH_KILL) * self.max_alpha),
            self.max_alpha
        )
