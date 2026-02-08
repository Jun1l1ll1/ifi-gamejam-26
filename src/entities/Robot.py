import pygame

from ..options import *
from ..assets import *

class Robot:
    all = []
    def __init__(self, x, y, rotation, room = CONTROL_ROOM_NAME):
        self.x = x
        self.y = y
        self.size = (70, 70)
        self.rotation = rotation
        self.image = pygame.transform.rotate(pygame.transform.scale(ROBOT_IMAGE, self.size), self.rotation)
        self.dialog = None
        self.dialog_offset = (80, -20)
        self.dialog_time = 0

        Robot.all.append((self, room))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        if self.dialog is not None:
            screen.blit(
                self.dialog,
                (self.x + self.dialog_offset[0], self.y + self.dialog_offset[1])
            )
    
    def can_interact(self, px, py, p_size):
        range = 50
        is_close = (self.x < px+p_size[0]+range and self.y < py+p_size[1]+range and self.x+self.size[0] > px-range and self.y+self.size[1] > py-range)
        return is_close
    
    def talk(self, current_time):
        self.dialog_time = current_time
        self.dialog = PLAYER_TIPS_FONT_TYPE.render("To cure the virus you need: \n\t Ginger from the Growth room \n\t Toothpaste from the Bathroom \n\t and Star Stone from the Airlock room\n\nThen go to the desk in the Laboratory \n\nHurry, before the virus grows!", False, FONT_COLOR)
    
    def remove_dialog(self):
        self.dialog = None
