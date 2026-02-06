import pygame

from .options import *


BACKGROUND_IMAGE = pygame.image.load('./assets/stars.jpg').convert()
AMONGUS_IMAGE = pygame.image.load('./assets/among.webp').convert_alpha()
BOULDER_IMAGE = pygame.image.load('./assets/boulder.png').convert_alpha()

# Font
FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', FONT_SIZE)