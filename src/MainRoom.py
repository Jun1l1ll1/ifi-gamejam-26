# from .options import *
# from .assets import *
from .Room import *

class MainRoom(Room):
    def __init__(self):
        self.doors = {
            "control_room": ((0, 220), (100, 500))
        }