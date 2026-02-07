# from .options import *
# from .assets import *
from ..Room import *

class GrowthRoom(Room):
    def __init__(self):
        super().__init__(
            {
                "main_room": ((0, 220), (100, 500))
            },
            ROOM_GARDEN_IMAGE
        )