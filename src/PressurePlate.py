import pygame

from .options import *
from .assets import *
from .Player import Player

class PressurePlate:
    def __init__(self, x, y):
        self.size = (71, 71)
        self.color = RED
        self.image = pygame.transform.scale(BOULDER_IMAGE, self.size)
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
        
    