# from .options import *
# from .assets import *
from ..Room import *
from ..objects.GingerPlant import *
from ..objects.PressurePlate import *

class GrowthRoom(Room):
    def __init__(self):
        super().__init__(
            GROWTH_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((0, 220), (100, 500)),
                LABORATORY_ROOM_NAME: ((400, 690), (800, 720)),
            },
            ROOM_GARDEN_IMAGE,
            {
                MAIN_ROOM_NAME: (20, HEIGHT//2-35),
                LABORATORY_ROOM_NAME: (WIDTH//2-35, HEIGHT-70 - 20)
            },
            [
                GingerPlant(700, 100),
                GingerPlant(700, 250),
                GingerPlant(700, 400),
                PressurePlate(500, 30, GROWTH_ROOM_NAME, "4")
            ]
        )