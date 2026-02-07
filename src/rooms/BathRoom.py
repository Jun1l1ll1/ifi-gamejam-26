# from .options import *
# from .assets import *
from ..Room import *
from ..PressurePlate import *

class BathRoom(Room):
    def __init__(self):
        super().__init__(
            BATH_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((400, 690), (800, 720))
            },
            ROOM_BATH_IMAGE,
            {},
            [ # Contents of the room:
                PressurePlate(100, 200, BATH_ROOM_NAME, "1"),
                PressurePlate(500, 100, BATH_ROOM_NAME),
                PressurePlate(900, 300, BATH_ROOM_NAME),
                PressurePlate(650, 500, BATH_ROOM_NAME),
                PressurePlate(800, 400, BATH_ROOM_NAME)
            ]
        )
