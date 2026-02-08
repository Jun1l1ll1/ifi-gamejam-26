# from .options import *
# from .assets import *
from ..Room import *
from ..objects.PressurePlate import *
from ..objects.Safe import *

class BathRoom(Room):
    def __init__(self):
        super().__init__(
            BATH_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((WIDTH//2-DOOR_WIDTH_RANGE, HEIGHT-DOOR_OUT_RANGE), (WIDTH//2+DOOR_WIDTH_RANGE, HEIGHT))
            },
            ROOM_BATH_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH//2-35, HEIGHT-70 - 20)
            },
            [ # Contents of the room:
                PressurePlate(850, 30, BATH_ROOM_NAME, "3"),
                Safe(750, 25)
            ],
            "Bathroom",
            [
                pygame.Rect(200, 0, 5, 230), #vegger

                pygame.Rect(390, 0, 5, 230),

                pygame.Rect(570, 0, 5, 230),

                pygame.Rect(1000, 0, 5, 720)
            ]
        )
