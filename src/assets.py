import pygame

from .options import *


BACKGROUND_IMAGE = pygame.image.load('./assets/stars.jpg').convert()
BOULDER_IMAGE = pygame.image.load('./assets/boulder.png').convert_alpha()

PLAYER1_IMAGE = pygame.image.load('./assets/player/Player1.png').convert_alpha()
PLAYER2_IMAGE = pygame.image.load('./assets/player/Player2.png').convert_alpha()
ROBOT_IMAGE = pygame.image.load('./assets/robot/Robot.png').convert_alpha()

ALIEN1_IMAGE = pygame.image.load('./assets/alien/Alien1.png').convert_alpha()
ALIEN2_IMAGE = pygame.image.load('./assets/alien/Alien2.png').convert_alpha()
ALIEN3_IMAGE = pygame.image.load('./assets/alien/Alien3.png').convert_alpha()
ALIEN4_IMAGE = pygame.image.load('./assets/alien/Alien4.png').convert_alpha()
ALIEN5_IMAGE = pygame.image.load('./assets/alien/Alien5.png').convert_alpha()

ROOM_CONTROL_IMAGE = pygame.image.load('./assets/rooms/ControlRoom.png').convert_alpha()
ROOM_BATH_IMAGE = pygame.image.load('./assets/rooms/BathRoom.png').convert_alpha()
ROOM_ENTRYEXIT_IMAGE = pygame.image.load('./assets/rooms/EntryExitRoom.png').convert_alpha()
ROOM_LABORATORY_IMAGE = pygame.image.load('./assets/rooms/LaboratoryRoom.png').convert_alpha()
ROOM_GARDEN_IMAGE = pygame.image.load('./assets/rooms/GardenRoom.png').convert_alpha()
ROOM_MAIN_IMAGE = pygame.image.load('./assets/rooms/MainRoom.png').convert_alpha()

GINGER_PLANT_EMPTY_IMAGE = pygame.image.load('./assets/ginger/GingerPlantEmpty.png').convert_alpha()
GINGER_PLANT_SMAL_IMAGE = pygame.image.load('./assets/ginger/GingerPlantSmal.png').convert_alpha()
GINGER_PLANT_BIG_IMAGE = pygame.image.load('./assets/ginger/GingerPlantBig.png').convert_alpha()
GINGER_IMAGE = pygame.image.load('./assets/ginger/Ginger.png').convert_alpha()

# Font
FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', FONT_SIZE)