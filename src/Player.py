import pygame

from .options import *
from .Projectile import Projectile
from .assets import *
import math as m

class Player:
    def __init__(self):
        self.x = 540
        self.y = 640
        self.size = (70, 70)
        self.color = BLUE
        self._base_image = pygame.transform.scale(PLAYER2_IMAGE, self.size)
        self.image = self._base_image
        self.speed = PLAYER_SPEED
        self.last_shot_time = 0

        self.virus_growth = 0

    def shoot(self):
        projectile = Projectile(self.x + self.size[0] // 2, self.y)
        return projectile

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def go_to(self, cords: tuple):
        self.x = cords[0]
        self.y = cords[1]
    
    def move(self, v: list[int], dt):
        length = self._normalize(v)
        if length <= 0: return

        self.image = pygame.transform.rotate(self._base_image, self._move_angle(v))

        self.x += self.speed * (v[0]/length) * dt
        self.y += self.speed * (v[1]/length) * dt

    def _normalize(self, v):
        return m.sqrt(v[0]**2 + v[1]**2)

    def _move_angle(self, v):
        u = [1, 0] # Sprite is rotated right by default
        dot_product = sum(i*j for i, j in zip(u, v))
        norm_u = self._normalize(u)
        norm_v = self._normalize(v)
        cos_theta = dot_product / (norm_u * norm_v)
        angle_rad = m.acos(cos_theta)

        dir = 1 # Make angle other way when going down
        if v[1] == 1: dir = -1

        return m.degrees(angle_rad) * dir
