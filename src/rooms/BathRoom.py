# from .options import *
# from .assets import *
from ..Room import *

class BathRoom(Room):
    def __init__(self):
        super().__init__(
            {
                "main_room": ((400, 690), (800, 720))
            },
            ROOM_BATH_IMAGE
        )