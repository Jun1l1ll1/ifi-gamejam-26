# from .options import *
# from .assets import *
from ..Room import *

class MainRoom(Room):
    def __init__(self):
        super().__init__(
            {
                "control_room": ((0, 220), (100, 500)),
                "bath_room": ((400, 0), (800, 200)),
                "growth_room": ((980, 220), (1080, 500)),
                "airlock_room": ((400, 690), (800, 720))
            },
            ROOM_MAIN_IMAGE
        )
        