import pygame

from ..options import *
from ..assets import *
from ..Player import *

class LabTable:
    all = []

    def __init__(self, x, y, room = LABORATORY_ROOM_NAME):
        self.x = x
        self.y = y
        self.size = (250, 150)
        self.image = pygame.transform.scale(LAB_TABLE_IMAGE, self.size)

        LabTable.all.append((self, room))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def can_interact(self, px, py, p_size):
        is_close = (self.x < px+p_size[0] and self.y < py+p_size[1] and self.x+self.size[0] > px and self.y+self.size[1] > py)
        return is_close
    
    def make_cure(self, player: Player):
        required_items = {GINGER, STAR_DUST, TOOTH_PASTE}
        if required_items.issubset(set(player.inventory)):
            for item in required_items:
                player.inventory.remove(item)
            player.collect(CURE)
        else:
            print(f"Missing: {required_items.difference(set(player.inventory)) }")
