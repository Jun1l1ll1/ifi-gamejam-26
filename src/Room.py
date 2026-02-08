import pygame

from .options import *
from .assets import *

class Room:
    def __init__(self, name, doors, room_img, entrance_cords_from_dict = {}, content = [], title = "", boundries = []):
        self.name = name
        self.doors = doors
        self.background = pygame.transform.scale(room_img, (WIDTH, HEIGHT))
        self.entrance_cords_from = entrance_cords_from_dict
        self.contents = content
        self.title = title
        self.boundries = boundries

    def open_door(self, px, py, p_size) -> str:
        for room in self.doors:
            cords = self.doors[room]# <<x,y>,<x,y>>

            top_left = cords[0] # <x,y>
            bottom_right = cords[1] # <x,y>

            if (top_left[0] < px+p_size[0] and px < bottom_right[0] and top_left[1] < py+p_size[1] and py < bottom_right[1]):
                return room
        return ""

    def get_enter_coords_from(self, last_room):
        coords = (WIDTH//2, HEIGHT//2)
        if last_room in self.entrance_cords_from:
            coords = self.entrance_cords_from[last_room]
        return coords
    
    def draw_content(self, screen):
        for content in self.contents:
            content.draw(screen)

    def can_move(self, px, py, v, p_size, dt):
        dx = v[0] * dt * PLAYER_SPEED
        dy = v[1] * dt * PLAYER_SPEED
        next_pos_rect = pygame.Rect(px + dx, py + dy, p_size[0], p_size[0])
        for boundry_rect in self.boundries:
            if next_pos_rect.colliderect(boundry_rect):
                return False
        return True
    