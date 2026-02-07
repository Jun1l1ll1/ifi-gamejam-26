# from .options import *
# from .assets import *
from .Room import *

class GrowthRoom(Room):
    def __init__(self):
        self.doors = {
            "main_room": ((0, 220), (100, 500))
        }