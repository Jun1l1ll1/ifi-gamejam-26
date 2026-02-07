import pygame

from ..options import *
from ..assets import *

class Robot:
    all = []
    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.size = (70, 70)
        self.rotation = rotation
        self.image = pygame.transform.rotate(pygame.transform.scale(ROBOT_IMAGE, self.size), self.rotation)

        Robot.all.append(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
