# from .options import *
# from .assets import *
from ..Room import *
from ..entities.Robot import *
from ..GingerPlant import *

class ControlRoom(Room):
    def __init__(self):
        super().__init__(
            CONTROL_ROOM_NAME,
            {
                MAIN_ROOM_NAME: ((980, 220), (1080, 500))
            },
            ROOM_CONTROL_IMAGE,
            {
                MAIN_ROOM_NAME: (WIDTH-70 - 20, HEIGHT//2-35)
            },
            [
                Robot(300, 450, 20)
            ]
        )