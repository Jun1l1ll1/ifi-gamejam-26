# from .options import *
# from .assets import *
from ..Room import *
from ..entities.Robot import *
from ..objects.GingerPlant import *
from ..objects.PressurePlate import *

class ControlRoom(Room):
    def __init__(self):
        super().__init__(
            CONTROL_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((WIDTH-DOOR_OUT_RANGE, HEIGHT//2-DOOR_WIDTH_RANGE), (WIDTH, HEIGHT//2+DOOR_WIDTH_RANGE))
            },
            ROOM_CONTROL_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH-70 - 20, HEIGHT//2-35)
            },
            [
                Robot(300, 450, 20),
                PressurePlate(850, 630, CONTROL_ROOM_NAME, "2")
            ],
            "Control Room", [

                pygame.Rect(340, 485, 20, 30)
                
                
            ]
        )