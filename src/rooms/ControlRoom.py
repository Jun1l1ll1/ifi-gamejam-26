# from .options import *
# from .assets import *
from ..Room import *

class ControlRoom(Room):
    def __init__(self):
        super().__init__(
            CONTROL_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((980, 220), (1080, 500))
            },
            ROOM_CONTROL_IMAGE
        )