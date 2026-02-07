# from .options import *
# from .assets import *
from ..Room import *

class LaboratoryRoom(Room):
    def __init__(self):
        super().__init__(
            {
                "growth_room": ((400, 0), (800, 200))
            },
            ROOM_LABORATORY_IMAGE
        )