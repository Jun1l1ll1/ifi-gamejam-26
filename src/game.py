""" Hovedprogrammet som skal kjøres """
import pygame
from .options import *

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py

import sys, random, time, os

from .assets import *
from .Player import Player
from .overlays.OverlayMessage import OverlayMessage
from .overlays.VirusGrowthOverlay import VirusGrowthOverlay
from .Boulder import Boulder
from .Projectile import Projectile
from .Room import Room
from .rooms.MainRoom import MainRoom
from .rooms.ControlRoom import ControlRoom
from .rooms.BathRoom import BathRoom
from .rooms.GrowthRoom import GrowthRoom
from .rooms.AirlockRoom import AirlockRoom
from .rooms.LaboratoryRoom import LaboratoryRoom


def run():
    pygame.display.set_caption("Virus game(First draft)")

    # Clock and timing
    clock = pygame.time.Clock()
    dt = 0
    last_boulder_spawn_time = 0
    last_virus_growth = 0

    # Game objects
    p1 = Player()
    virus_growing_msg = OverlayMessage("The virus is growing", 250)
    virus_growth_overlay = VirusGrowthOverlay()
    projectiles = []
    boulders = []

    ROOMS = {
        CONTROL_ROOM_NAME: ControlRoom(),
        MAIN_ROOM_NAME: MainRoom(),
        BATH_ROOM_NAME: BathRoom(),
        GROWTH_ROOM_NAME: GrowthRoom(),
        AIRLOCK_ROOM_NAME: AirlockRoom(),
        LABORATORY_ROOM_NAME: LaboratoryRoom()
    }

    current_room: Room = ROOMS[MAIN_ROOM_NAME]

    score = 0

    def draw_frame():
        screen.blit(current_room.background, (0, 0))
        
        # Player
        p1.draw(screen)

        # Purple Virus growth overlay
        virus_growth_overlay.draw(screen)

        # Virus is growing message
        if virus_growing_msg.show:
            virus_growing_msg.draw(screen)
        
        '''
        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)
        for boulder in boulders:
            boulder.draw(screen)
            
        # Draw score and lives
        score_text = FONT_TYPE.render(f'Score: {score}', False, FONT_COLOR)
        lives_text = FONT_TYPE.render(f"♥"*p1.virus_growth, True, FONT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
        '''

        pygame.display.flip()

    # Game loop
    running = True
    while running:
        clock.tick(FRAMERATE)  # Limit frame rate
        current_time = pygame.time.get_ticks()

        # Game ends
        if p1.virus_growth >= VIRUS_GROWTH_KILL:
            running = False #TODO Change to game end screen?

        # Virus growth
        if current_time - last_virus_growth >= VIRUS_GROWTH_COOLDOWN_MS:
            last_virus_growth = current_time
            p1.virus_growth += 1
            virus_growth_overlay.increse_alpha(p1.virus_growth)
            virus_growing_msg.show = True
        elif virus_growing_msg.show and current_time - last_virus_growth >= VIRUS_GROWTH_DISPLAY_MSG_TIME_MS:
            virus_growing_msg.show = False

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()

        # Move player
        v = [0, 0] # Player velocity "vector"
        if keys[pygame.K_a]: 
            if not p1.x <= 0:
                v[0] -= 1
        if keys[pygame.K_d]:
            if not p1.x >= WIDTH - p1.size[0]:
                v[0] += 1
        if keys[pygame.K_w]: 
            if not p1.y <= 0:
                v[1] -= 1
        if keys[pygame.K_s]: 
            if not p1.y >= HEIGHT - p1.size[1]:
                v[1] += 1
        p1.move(v, dt)

        # Handle doors and change location
        door = current_room.open_door(p1.x, p1.y, p1.size)
        if door != "" and keys[pygame.K_e]:
            enter_cords = current_room.get_enter_coords_from(current_room.name)
            current_room = ROOMS[door]
            p1.go_to(enter_cords)

        # Shooting
        if keys[pygame.K_SPACE]:
            if current_time - p1.last_shot_time >= BULLET_COOLDOWN_MS:
                p1.last_shot_time = current_time
                projectile = p1.shoot()
                projectiles.append(projectile)

        '''
        # Boulder spawning
        if current_time - last_boulder_spawn_time >= BOULDER_SPAWN_INTERVAL_MS:
            boulder = Boulder()
            boulders.append(boulder)
            last_boulder_spawn_time = current_time

        # Progectile movement
        for projectile in projectiles:
            if projectile.y <= 0:
                projectiles.remove(projectile)
            projectile.update(dt)
            # collision w boulder
            for boulder in boulders:
                if projectile.collides_with(boulder.get_rect()):
                    projectiles.remove(projectile)
                    boulders.remove(boulder)
                    score += 100
                    break

        # Boulder movement
        for boulder in boulders:
            boulder.y += boulder.speed * dt
            if boulder.y >= HEIGHT + boulder.size[1]:
                boulders.remove(boulder)
                p1.lives -= 1
                if p1.lives <= 0:
                    # Game over sequence
                    boulders.clear()
                    projectiles.clear()
                    draw_frame()
                    game_over_text = FONT_TYPE.render("GAME OVER", True, RED)
                    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(2)
                    running = False
        '''

        # Update display
        draw_frame()

        dt = clock.tick(60) / 1000

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
