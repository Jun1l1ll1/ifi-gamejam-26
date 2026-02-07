# from .options import *
# from .assets import *
from ..Room import *
from ..entities.CagedAlien import *

class LaboratoryRoom(Room):
    def __init__(self):
        super().__init__(
            LABORATORY_ROOM_NAME,
            {
                GROWTH_ROOM_NAME: ((400, 0), (800, 200))
            },
            ROOM_LABORATORY_IMAGE,
            {},
            [
                CagedAlien(700, 50)
            ]
        )