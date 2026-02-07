import pygame

from .options import *
from .Projectile import Projectile
from .assets import *
import math as m

class Player:
    def __init__(self):
        self.x = 540
        self.y = 640
        self.size = (40, 50)
        self.color = BLUE
        self.image = pygame.transform.scale(PLAYER2_IMAGE, self.size)
        self.speed = PLAYER_SPEED
        self.last_shot_time = 0

        self.lives = LIVES

    def shoot(self):
        projectile = Projectile(self.x + self.size[0] // 2, self.y)
        return projectile

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def move(self, v: list[int], dt):
        length = m.sqrt(v[0]**2 + v[1]**2)
        if length <= 0: return

        self.x += self.speed * (v[0]/length) * dt
        self.y += self.speed * (v[1]/length) * dt