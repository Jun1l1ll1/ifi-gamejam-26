import pygame
from ..options import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

import sys, random, time, os

from ..assets import *
from .rocket import Rocket
from ..Boulder import Boulder
from ..Projectile import Projectile


def run():
    pygame.display.set_caption("'Rocket' - minigame")

    clock = pygame.time.Clock()
    dt = 0
    last_boulder_spawn_time = 0

    p1 = Rocket()
    projectiles = []
    boulders = []

    STAR_STONES_REQUIRED = 5
    star_stones_collected = 0
    task_completed = False

    def draw_frame():
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        pygame.draw.rect(screen, BLACK, (0, 690, WIDTH, 30))
        p1.draw(screen)

        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)

        for boulder in boulders:
            boulder.draw(screen)

        progress_text = FONT_TYPE.render(
            f"Star-stones: {star_stones_collected}/{STAR_STONES_REQUIRED}",
            False,
            FONT_COLOR
        )
        lives_text = FONT_TYPE.render(f"♥" * p1.lives, True, FONT_COLOR)

        screen.blit(progress_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))

        pygame.display.flip()

    running = True
    while running:
        clock.tick(FRAMERATE)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            p1.x -= p1.speed * dt
        if keys[pygame.K_d]:
            p1.x += p1.speed * dt
        if keys[pygame.K_SPACE]:
            if current_time - p1.last_shot_time >= BULLET_COOLDOWN_MS:
                p1.last_shot_time = current_time
                projectiles.append(p1.shoot())

        if current_time - last_boulder_spawn_time >= BOULDER_SPAWN_INTERVAL_MS:
            boulders.append(Boulder())
            last_boulder_spawn_time = current_time

        for projectile in projectiles[:]:
            if projectile.y <= 0:
                projectiles.remove(projectile)
                continue

            projectile.update(dt)
            for boulder in boulders[:]:
                if projectile.collides_with(boulder.get_rect()):
                    projectiles.remove(projectile)
                    boulders.remove(boulder)
                    star_stones_collected += 1

                    if star_stones_collected >= STAR_STONES_REQUIRED:
                        task_completed = True
                        running = False
                    break

        for boulder in boulders[:]:
            boulder.y += boulder.speed * dt
            if boulder.y >= HEIGHT + boulder.size[1]:
                boulders.remove(boulder)
                p1.lives -= 1
                if p1.lives <= 0:
                    running = False

        draw_frame()
        dt = clock.tick(60) / 1000

    if task_completed:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        success_text = FONT_TYPE.render("TASK COMPLETED!", True, GREEN)
        sub_text = FONT_TYPE.render("All star-stones collected", True, FONT_COLOR)

        screen.blit(success_text, (WIDTH // 2 - success_text.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 + 10))

        pygame.display.flip()
        time.sleep(2)

    return


if __name__ == "__main__":
    run()
