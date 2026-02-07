from .options import *

class Projectile:
    def __init__(self, x, y, direction: list[int] = [0, -1]):
        self.x = x
        self.y = y
        self.size = (10, 10)
        self.speed = BULLET_SPEED
        self.color = GREEN
        self.dir = direction # Normalized direction-vector
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1]) #TODO rotate bullet rect

    def update(self, dt):
        self.y += self.dir[1] * self.speed * dt
        self.x += self.dir[0] * self.speed * dt
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size[0], self.size[1]))

    def collides_with(self, boulder_rect):
        return self.rect.colliderect(boulder_rect)