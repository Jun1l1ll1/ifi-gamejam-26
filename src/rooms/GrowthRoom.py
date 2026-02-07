# from .options import *
# from .assets import *
from ..Room import *
from ..GingerPlant import *

class GrowthRoom(Room):
    def __init__(self):
        super().__init__(
            GROWTH_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((0, 220), (100, 500)),
                LABORATORY_ROOM_NAME: ((400, 690), (800, 720)),
            },
            ROOM_GARDEN_IMAGE,
            {},
            [
                GingerPlant(700, 100),
                GingerPlant(700, 250),
                GingerPlant(700, 400)
            ]
        )