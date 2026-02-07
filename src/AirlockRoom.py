# from .options import *
# from .assets import *
from .Room import *

class AirlockRoom(Room):
    def __init__(self):
        self.doors = {
            "main_room": ((400, 0), (800, 200)),
        }