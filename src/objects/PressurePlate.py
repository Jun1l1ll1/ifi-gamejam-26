import pygame

from ..options import *
from ..assets import *
from ..Player import Player

class PressurePlate:
    all_pressure_plates = []

    def __init__(self, x, y, room, text = ""):
        self.size = (71, 71)
        self.x = x
        self.y = y
        self.color = RED
        self.image = pygame.transform.scale(BOULDER_IMAGE, self.size)
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.text = text
        self.font = FONT_TYPE.render(text, False, FONT_COLOR)

        self.activated = False
        PressurePlate.all_pressure_plates.append((self, room))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.activated:
            pygame.draw.rect(screen, GREEN, self.rect)
        else: 
            pygame.draw.rect(screen, RED, self.rect)

        screen.blit(self.font, (self.x + self.size[0]/2 - 7, self.y + self.size[1]/2 - 12))

    
        
    