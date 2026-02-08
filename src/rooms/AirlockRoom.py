# from .options import *
# from .assets import *
from ..Room import *
from ..objects.PressurePlate import *

class AirlockRoom(Room):
    def __init__(self):
        super().__init__(
            AIRLOCK_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((400, 0), (800, 200))
            },
            ROOM_AIRLOCK_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH//2-35, 20)
            },
            [
                PressurePlate(20, 600, AIRLOCK_ROOM_NAME, "5")
            ]
        )