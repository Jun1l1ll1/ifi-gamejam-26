import pygame

from ..options import *
from ..assets import *
import math as m

class CagedAlien:
    instance = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (200, 170)
        self.rotation = -30
        self.image = pygame.transform.rotate(pygame.transform.scale(ALIEN1_IMAGE, self.size), self.rotation)
        self.growth = 1

        CagedAlien.instance = self

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def grow(self, virus_growth):
        self.growth = m.floor((virus_growth+1)/VIRUS_GROWTH_KILL * MAX_ALIEN_GROWTH)

        img = self.image
        match self.growth:
            case 1:
                img = ALIEN1_IMAGE
            case 2:
                img = ALIEN2_IMAGE
            case 3:
                img = ALIEN3_IMAGE
            case 4:
                img = ALIEN4_IMAGE
            case 5:
                img = ALIEN5_IMAGE

        self.image = pygame.transform.rotate(pygame.transform.scale(img, self.size), self.rotation)

