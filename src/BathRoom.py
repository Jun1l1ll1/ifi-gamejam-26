# from .options import *
# from .assets import *
from .Room import *

class BathRoom(Room):
    def __init__(self):
        self.doors = {
            "main_room": ((400, 690), (800, 720))
        }