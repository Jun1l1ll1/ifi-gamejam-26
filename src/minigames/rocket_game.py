import pygame
from ..options import *

pygame.init()

import sys, random, time, os

from ..assets import *
from .rocket import Rocket
from .Boulder import Boulder
from ..Projectile import Projectile


def run(screen):

    pygame.display.set_caption("'Rocket' - minigame")

    # Minigame hover size (shrunken version of main game)
    HOVER_SCALE = 0.85  # 85% of main game size
    MINIGAME_WIDTH = int(WIDTH * HOVER_SCALE)
    MINIGAME_HEIGHT = int(HEIGHT * HOVER_SCALE)
    hover_x = (WIDTH - MINIGAME_WIDTH) // 2
    hover_y = (HEIGHT - MINIGAME_HEIGHT) // 2

    # Surface for minigame logic
    minigame_surface = pygame.Surface((WIDTH, HEIGHT))  # logic uses full size

    clock = pygame.time.Clock()
    dt = 0
    last_boulder_spawn_time = 0

    # Game objects
    p1 = Rocket()
    projectiles = []
    boulders = []

    STAR_STONES_REQUIRED = 5
    star_stones_collected = 0
    task_completed = False

    def draw_frame():
        # Draw everything to minigame_surface
        minigame_surface.blit(BACKGROUND_IMAGE, (0, 0))
        pygame.draw.rect(minigame_surface, BLACK, (0, 690, WIDTH, 30))
        p1.draw(minigame_surface)

        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(minigame_surface)

        for boulder in boulders:
            boulder.draw(minigame_surface)

        progress_text = FONT_TYPE.render(
            f"Star-stones: {star_stones_collected}/{STAR_STONES_REQUIRED}",
            False,
            FONT_COLOR
        )
        lives_text = FONT_TYPE.render(f"♥" * p1.lives, True, FONT_COLOR)

        minigame_surface.blit(progress_text, (10, 10))
        minigame_surface.blit(lives_text, (WIDTH - 120, 10))

        # Scale minigame for hovering effect
        scaled_surface = pygame.transform.smoothscale(minigame_surface, (MINIGAME_WIDTH, MINIGAME_HEIGHT))
        screen.blit(scaled_surface, (hover_x, hover_y))

    running = True
    while running:
        dt = clock.tick(FRAMERATE) / 1000
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

        # Spawn boulders
        if current_time - last_boulder_spawn_time >= BOULDER_SPAWN_INTERVAL_MS:
            boulders.append(Boulder())
            last_boulder_spawn_time = current_time

        # Handle projectiles hitting boulders
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

        # Update boulders falling
        for boulder in boulders[:]:
            boulder.y += boulder.speed * dt
            if boulder.y >= HEIGHT + boulder.size[1]:
                boulders.remove(boulder)
                p1.lives -= 1
                if p1.lives <= 0:
                    failed = True
                    running = False

        draw_frame()
        pygame.display.update()  # refresh main game screen with minigame on top

    # Optional success message
    if task_completed:
        minigame_surface.blit(BACKGROUND_IMAGE, (0, 0))
        success_text = FONT_TYPE.render("TASK COMPLETED!", True, GREEN)
        sub_text = FONT_TYPE.render("All star-stones collected", True, FONT_COLOR)
        sub_text = FONT_TYPE.render("Proceed.", True, FONT_COLOR)

        minigame_surface.blit(success_text, (WIDTH // 2 - success_text.get_width() // 2, HEIGHT // 2 - 40))
        minigame_surface.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 + 10))

        scaled_surface = pygame.transform.smoothscale(minigame_surface, (MINIGAME_WIDTH, MINIGAME_HEIGHT))
        screen.blit(scaled_surface, (hover_x, hover_y))
        pygame.display.update()
        time.sleep(2)


    elif failed:
        minigame_surface.blit(BACKGROUND_IMAGE, (0, 0))
        game_over_text = FONT_TYPE.render("GAME OVER", True, (255, 0, 0))
        sub_text = FONT_TYPE.render("You failed the task", True, FONT_COLOR)

        minigame_surface.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 40))
        minigame_surface.blit(sub_text, (WIDTH//2 - sub_text.get_width()//2, HEIGHT//2 + 10))

        # Scale and hover
        scaled_surface = pygame.transform.smoothscale(minigame_surface, (MINIGAME_WIDTH, MINIGAME_HEIGHT))
        screen.blit(scaled_surface, (hover_x, hover_y))
        pygame.display.update()
        time.sleep(2)


    return task_completed





if __name__ == "__main__":
    run()
