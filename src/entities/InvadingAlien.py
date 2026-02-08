import pygame
import random
import math
from ..assets import *

RED = (255, 0, 0)

class InvadingAlien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = (100, 100)
        self._base_image = pygame.transform.scale(INVADING_ALIEN_IMAGE, self.size)
        self.image = self._base_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 800)
        self.speed = random.uniform(60, 120)
        self.max_health = 30
        self.health = self.max_health
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def draw_healthbar(self, screen):
        bar_width = self.rect.width
        bar_height = 6

        health_ratio = self.health / self.max_health
        
        #Rød background
        bg = pygame.Rect(self.rect.x, self.rect.y - bar_height - 4, bar_width, bar_height)
        #Grønn forground
        fg = pygame.Rect(self.rect.x, self.rect.y - bar_height - 4, bar_width * health_ratio, bar_height)

        #background
        pygame.draw.rect(screen, (120, 0, 0), bg)
        #health
        pygame.draw.rect(screen, (0, 200, 0), fg)

    def take_damage(self, amount):
        self.health -= amount
        

    def update(self, player_rect, dt):
        #Finner retning mot spiller
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)
        if distance == 0:
            return
        
        #Normaliser retning
        dx /= distance
        dy /= distance

        #Beveger seg som en "zombie/alien"
        dx += random.uniform(-0.02, 0.02)
        dy += random.uniform(-0.02, 0.02)

        length = math.hypot(dx, dy)
        if length == 0: return

        dx /= length
        dy /= length

        #Beveg mot player
        self.rect.x += dx * self.speed * dt
        self.rect.y += dy * self.speed * dt

        v = [dx, dy]


        self.image = pygame.transform.rotate(self._base_image, self._move_angle(v))

    def _length(self, v):
       return math.sqrt(v[0]**2 + v[1]**2)

    def _move_angle(self, v):
        u = [1, 0] # Sprite is rotated right by default
        dot_product = sum(i*j for i, j in zip(u, v))
        norm_u = self._length(u)
        norm_v = self._length(v)
        cos_theta = dot_product / (norm_u * norm_v)
        angle_rad = math.acos(cos_theta)

        dir = 1 # Make angle other way when going down
        if v[1] > 0: dir = -1

        return math.degrees(angle_rad) * dir


