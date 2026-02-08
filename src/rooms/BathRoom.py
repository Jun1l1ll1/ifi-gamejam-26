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
                MAIN_ROOM_NAME: ((400, 690), (800, 720))
            },
            ROOM_BATH_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH//2-35, HEIGHT-70 - 20)
            },
            [ # Contents of the room:
                PressurePlate(850, 30, BATH_ROOM_NAME, "3"),
                Safe(20, 600)
            ]
        )
