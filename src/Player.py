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
        self.inventory = []        
        self.max_health = 100
        self.health = self.max_health
        self.last_hit_time = 0
        self.hit_cooldown = 700 #ms
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0


    def shoot(self):
        projectile = Projectile(self.x + self.size[0] // 2, self.y)
        return projectile
    
    def collect(self, item):
        if item == "": return # Don't add nothing
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"Added: {item} to inventory")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def draw_healthbar(self, screen):
        bar_width = 60
        bar_height = 8

        health_ratio = self.health / self.max_health
        fill_width = int(bar_width * health_ratio)

        x = self.x + (self.size[0] - bar_width) // 2
        y = self.y - 12

        #background
        pygame.draw.rect(screen, (60, 60, 60), (x, y, bar_width, bar_height))
        #health
        pygame.draw.rect(screen, (0, 200, 0), (x, y, fill_width, bar_height))

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
