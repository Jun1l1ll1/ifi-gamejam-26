import pygame
import random
import math

RED = (255, 0, 0)

class InvadingAlien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 800)
        self.speed = random.uniform(60, 120)
    
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

        #Beveg mot player
        self.rect.x += dx * self.speed * dt
        self.rect.y += dy * self.speed * dt

        #Beveger seg som en "zombie/alien"
        dx += random.uniform(-0.1, 0.1)
        dy += random.uniform(-0.1, 0.1)
