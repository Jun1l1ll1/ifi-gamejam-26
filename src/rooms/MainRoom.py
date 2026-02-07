# from .options import *
# from .assets import *
from ..Room import *

class MainRoom(Room):
    def __init__(self):
        super().__init__(
            MAIN_ROOM_NAME,
            {
                CONTROL_ROOM_NAME: ((0, 220), (100, 500)),
                BATH_ROOM_NAME: ((400, 0), (800, 200)),
                GROWTH_ROOM_NAME: ((980, 220), (1080, 500)),
                AIRLOCK_ROOM_NAME: ((400, 690), (800, 720))
            },
            ROOM_MAIN_IMAGE
        )
        