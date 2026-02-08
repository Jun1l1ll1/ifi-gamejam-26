# from .options import *
# from .assets import *
from ..Room import *
from ..objects.PressurePlate import *
from ..objects.LazerControler import *

class AirlockRoom(Room):
    def __init__(self):
        super().__init__(
            AIRLOCK_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((WIDTH//2-DOOR_WIDTH_RANGE, 0), (WIDTH//2+DOOR_WIDTH_RANGE, DOOR_OUT_RANGE))
            },
            ROOM_AIRLOCK_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH//2-35, 20)
            },
            [
                PressurePlate(20, 600, AIRLOCK_ROOM_NAME, "5"),
                LazerControler(200, 625)
            ],
            "Airlock Room", 
            [
                pygame.Rect(210, 630, 65, 15)
            ]
        )
    
    def invade(self):
        self.background = pygame.transform.scale(ROOM_AIRLOCK_INVADED_IMAGE, (WIDTH, HEIGHT))