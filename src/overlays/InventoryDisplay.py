import pygame

from ..options import *
from ..assets import *

class InventoryDisplay:
    def __init__(self):
        self.slot_size = (70, 70)
        self.x, self.y = 0, 0
        self.spacing = 10

    def draw(self, screen, items: list[str]):
        if len(items) < 0: return
        background = pygame.Surface(((self.slot_size[0] + self.spacing)*len(items) + self.spacing, self.slot_size[1]))
        background.set_alpha(175) # Make background transparent
        screen.blit(background, (self.x, self.y))
        for i in range(len(items)):
            item = items[i]
            screen.blit(self._get_item_img(item), ((self.slot_size[0] + self.spacing)*i + self.spacing + self.x, self.y))
    
    def _get_item_img(self, item):
        img = ROBOT_IMAGE
        if item == GINGER:
            img = GINGER_IMAGE
        elif item == STAR_DUST:
            img = STAR_STONE_IMAGE
        elif item == TOOTH_PASTE:
            img = TOOTH_PASTE_IMAGE
        elif item == CURE:
            pass
        return pygame.transform.scale(img, self.slot_size)
        
