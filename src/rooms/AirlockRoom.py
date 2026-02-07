# from .options import *
# from .assets import *
from ..Room import *

class AirlockRoom(Room):
    def __init__(self):
        super().__init__(
            {
                "main_room": ((400, 0), (800, 200))
            },
            ROOM_AIRLOCK_IMAGE
        )