# from .options import *
# from .assets import *
from .Room import *

class LaboratoryRoom(Room):
    def __init__(self):
        self.doors = {
            "growth_room": ((400, 0), (800, 200)),
        }