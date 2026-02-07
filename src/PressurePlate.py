import pygame

from .options import *
from .assets import *
from .Player import Player

class PressurePlate:
    all_pressure_plates = []

    def __init__(self, x, y, room):
        self.size = (71, 71)
        self.color = RED
        self.image = pygame.transform.scale(BOULDER_IMAGE, self.size)
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])

        self.activated = False
        PressurePlate.all_pressure_plates.append((self, room))

        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.activated:
            pygame.draw.rect(screen, GREEN, self.rect)
        else: 
            pygame.draw.rect(screen, RED, self.rect)

    
        
    