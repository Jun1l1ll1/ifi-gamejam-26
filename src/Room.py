import pygame

from .options import *
from .assets import *

class Room:
    def __init__(self, doors, room_img):
        self.doors = doors
        self.background = pygame.transform.scale(room_img, (WIDTH, HEIGHT))

    def open_door(self, px, py, p_size) -> str:
        for room in self.doors:
            cords = self.doors[room]# <<x,y>,<x,y>>

            top_left = cords[0] # <x,y>
            bottom_right = cords[1] # <x,y>

            if (top_left[0] < px+p_size[0] and px < bottom_right[0] and top_left[1] < py+p_size[1] and py < bottom_right[1]):
                return room
        return ""
    
    def enter(self):
        print("entered")
