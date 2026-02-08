# from .options import *
# from .assets import *
from ..Room import *
from ..entities.CagedAlien import *
from ..objects.LabTable import *
from ..objects.PressurePlate import *
from ..SafeHint import *

class LaboratoryRoom(Room):
    def __init__(self):
        super().__init__(
            LABORATORY_ROOM_NAME,
            {
                GROWTH_ROOM_NAME: ((490, 70), (590, 170))
            },
            ROOM_LABORATORY_IMAGE,
            {
                GROWTH_ROOM_NAME: (WIDTH//2-35, 20)
            },
            [
                CagedAlien(700, 50),
                LabTable(50, HEIGHT-200),
                PressurePlate(300, 600, LABORATORY_ROOM_NAME, "1"),
                SafeHint(WIDTH-450, HEIGHT-100)
            ]
        )