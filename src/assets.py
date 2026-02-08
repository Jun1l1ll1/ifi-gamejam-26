import pygame

from .options import *


BACKGROUND_IMAGE = pygame.image.load('./assets/stars.jpg').convert_alpha()
BOULDER_IMAGE = pygame.image.load('./assets/boulder.png').convert_alpha()
ROCKET_IMAGE = pygame.image.load('./assets/rocket.png').convert_alpha()

PLAYER1_IMAGE = pygame.image.load('./assets/player/Player1.png').convert_alpha()
PLAYER2_IMAGE = pygame.image.load('./assets/player/Player2.png').convert_alpha()
ROBOT_IMAGE = pygame.image.load('./assets/robot/Robot.png').convert_alpha()

ALIEN1_IMAGE = pygame.image.load('./assets/alien/Alien1.png').convert_alpha()
ALIEN2_IMAGE = pygame.image.load('./assets/alien/Alien2.png').convert_alpha()
ALIEN3_IMAGE = pygame.image.load('./assets/alien/Alien3.png').convert_alpha()
ALIEN4_IMAGE = pygame.image.load('./assets/alien/Alien4.png').convert_alpha()
ALIEN5_IMAGE = pygame.image.load('./assets/alien/Alien5.png').convert_alpha()

INVADING_ALIEN_IMAGE = pygame.image.load('./assets/alien/InvadingAlien.png').convert_alpha()

ROOM_CONTROL_IMAGE = pygame.image.load('./assets/rooms/ControlRoom.png').convert_alpha()
ROOM_BATH_IMAGE = pygame.image.load('./assets/rooms/BathRoom.png').convert_alpha()
ROOM_AIRLOCK_IMAGE = pygame.image.load('./assets/rooms/AirlockRoom.png').convert_alpha()
ROOM_LABORATORY_IMAGE = pygame.image.load('./assets/rooms/LaboratoryRoom.png').convert_alpha()
ROOM_GARDEN_IMAGE = pygame.image.load('./assets/rooms/GardenRoom.png').convert_alpha()
ROOM_MAIN_IMAGE = pygame.image.load('./assets/rooms/MainRoom.png').convert_alpha()

GINGER_PLANT_EMPTY_IMAGE = pygame.image.load('./assets/ginger/GingerPlantEmpty.png').convert_alpha()
GINGER_PLANT_SMAL_IMAGE = pygame.image.load('./assets/ginger/GingerPlantSmal.png').convert_alpha()
GINGER_PLANT_BIG_IMAGE = pygame.image.load('./assets/ginger/GingerPlantBig.png').convert_alpha()
GINGER_IMAGE = pygame.image.load('./assets/items/Ginger.png').convert_alpha()

LAB_TABLE_IMAGE = pygame.image.load('./assets/lab_equipment/LabDesk.png').convert_alpha()

STAR_COMET_IMAGE = pygame.image.load('./assets/rocket_minigame/StarStoneComet.png').convert_alpha()
STAR_STONE_IMAGE = pygame.image.load('./assets/items/StarStone.png').convert_alpha()

TOOTH_PASTE_IMAGE = pygame.image.load('./assets/items/ToothPaste.png').convert_alpha()

# Font
FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', FONT_SIZE)