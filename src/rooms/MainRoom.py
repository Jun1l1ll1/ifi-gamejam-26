# from .options import *
# from .assets import *
from ..Room import *
from ..objects.PressurePlate import *

class MainRoom(Room):
    def __init__(self):
        super().__init__(
            MAIN_ROOM_NAME,
            {
                CONTROL_ROOM_NAME: ((0, HEIGHT//2-DOOR_WIDTH_RANGE), (DOOR_OUT_RANGE, HEIGHT//2+DOOR_WIDTH_RANGE)),
                BATH_ROOM_NAME: ((WIDTH//2-DOOR_WIDTH_RANGE, 0), (WIDTH//2+DOOR_WIDTH_RANGE, DOOR_OUT_RANGE)),
                GROWTH_ROOM_NAME: ((WIDTH-DOOR_OUT_RANGE, HEIGHT//2-DOOR_WIDTH_RANGE), (WIDTH, HEIGHT//2+DOOR_WIDTH_RANGE)),
                AIRLOCK_ROOM_NAME: ((WIDTH//2-DOOR_WIDTH_RANGE, HEIGHT-DOOR_OUT_RANGE), (WIDTH//2+DOOR_WIDTH_RANGE, HEIGHT))
            },
            ROOM_MAIN_IMAGE,
            {
                CONTROL_ROOM_NAME: (20, HEIGHT//2-35),
                BATH_ROOM_NAME: (WIDTH//2-35, 20),
                GROWTH_ROOM_NAME: (WIDTH-70 - 20, HEIGHT//2-35),
                AIRLOCK_ROOM_NAME: (WIDTH//2-35, HEIGHT-70 - 20)
            },
            [],
            "Main Room"
         
        )
        