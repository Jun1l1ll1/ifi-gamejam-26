import pygame

from .options import *

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

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
ROOM_AIRLOCK_INVADED_IMAGE = pygame.image.load('./assets/rooms/AirlockRoomInvaded.png').convert_alpha()
ROOM_LABORATORY_IMAGE = pygame.image.load('./assets/rooms/LaboratoryRoom.png').convert_alpha()
ROOM_GARDEN_IMAGE = pygame.image.load('./assets/rooms/GardenRoom.png').convert_alpha()
ROOM_MAIN_IMAGE = pygame.image.load('./assets/rooms/MainRoom.png').convert_alpha()

PRESSURE_PLATE_ACTIVE_IMAGE = pygame.image.load('./assets/pressure_plate/PressurePlateActive.png').convert_alpha()
PRESSURE_PLATE_INACTIVE_IMAGE = pygame.image.load('./assets/pressure_plate/PressurePlateInactive.png').convert_alpha()

GINGER_PLANT_EMPTY_IMAGE = pygame.image.load('./assets/ginger/GingerPlantEmpty.png').convert_alpha()
GINGER_PLANT_SMAL_IMAGE = pygame.image.load('./assets/ginger/GingerPlantSmal.png').convert_alpha()
GINGER_PLANT_BIG_IMAGE = pygame.image.load('./assets/ginger/GingerPlantBig.png').convert_alpha()
GINGER_IMAGE = pygame.image.load('./assets/items/Ginger.png').convert_alpha()
WATERING_TERMINAL_ACTIVE_IMAGE = pygame.image.load('./assets/typing_minigame/WateringTerminalGreen.png').convert_alpha()
WATERING_TERMINAL_INACTIVE_IMAGE = pygame.image.load('./assets/typing_minigame/WateringTerminalRed.png').convert_alpha()

LAB_TABLE_IMAGE = pygame.image.load('./assets/lab_equipment/LabDesk.png').convert_alpha()

LAZER_CONTROLER_IMAGE = pygame.image.load('./assets/rocket_minigame/LazerControler.png').convert_alpha()
STAR_COMET_IMAGE = pygame.image.load('./assets/rocket_minigame/StarStoneComet.png').convert_alpha()
STAR_STONE_IMAGE = pygame.image.load('./assets/items/StarStone.png').convert_alpha()

SAFE_LOCKED_IMAGE = pygame.image.load('./assets/safe/SafeLocked.png').convert_alpha()
SAFE_OPEN_IMAGE = pygame.image.load('./assets/safe/SafeOpen.png').convert_alpha()
TOOTH_PASTE_IMAGE = pygame.image.load('./assets/items/ToothPaste.png').convert_alpha()

# Story frames
STORY1_FRAME1_IMAGE = pygame.image.load('./assets/story/Story1Frame1.png').convert_alpha()
STORY1_FRAME2_IMAGE = pygame.image.load('./assets/story/Story1Frame2.png').convert_alpha()
STORY1_FRAME3_IMAGE = pygame.image.load('./assets/story/Story1Frame3.png').convert_alpha()
STORY1_FRAME4_IMAGE = pygame.image.load('./assets/story/Story1Frame4.png').convert_alpha()

# Helping images
KEY_E_IMAGE = pygame.image.load('./assets/helper_icons/KeyE.png').convert_alpha()
KEY_W_IMAGE = pygame.image.load('./assets/helper_icons/KeyW.png').convert_alpha()
KEY_A_IMAGE = pygame.image.load('./assets/helper_icons/KeyA.png').convert_alpha()
KEY_S_IMAGE = pygame.image.load('./assets/helper_icons/KeyS.png').convert_alpha()
KEY_D_IMAGE = pygame.image.load('./assets/helper_icons/KeyD.png').convert_alpha()

# Font
FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', FONT_SIZE)
TITLE_FONT = pygame.font.Font('./assets/dpcomic.ttf', 96)
START_FONT = pygame.font.Font('./assets/dpcomic.ttf', 36)

# Sound
TITLE_SOUND = pygame.mixer.music.load("./assets/sounds/Intro_music.mp3")
INGAME_SOUND = pygame.mixer.music.load("./assets/sounds/Ingame_music.mp3")
PLAYER_TIPS_FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', PLAYER_TIPS_FONT_SIZE)

