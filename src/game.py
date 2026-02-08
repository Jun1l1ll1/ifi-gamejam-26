import pygame
from .minigames.rocket_game import run as run_rocket_game
from .minigames.typing_game import run as run_typing_game

from .options import *

# Init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Needed here by assets.py

import sys, random, time, os

from .assets import *
from .Player import Player
from .overlays.OverlayMessage import OverlayMessage
from .overlays.VirusGrowthOverlay import VirusGrowthOverlay
from .overlays.InventoryDisplay import InventoryDisplay
from .minigames.Boulder import Boulder
from .Projectile import Projectile
from .Room import Room
from .rooms.MainRoom import MainRoom
from .rooms.ControlRoom import ControlRoom
from .rooms.BathRoom import BathRoom
from .rooms.GrowthRoom import GrowthRoom
from .rooms.AirlockRoom import AirlockRoom
from .rooms.LaboratoryRoom import LaboratoryRoom
from .objects.PressurePlate import PressurePlate
from .entities.CagedAlien import CagedAlien
from .objects.GingerPlant import GingerPlant
from .objects.Safe import Safe
from .objects.LabTable import LabTable
from .entities.InvadingAlien import InvadingAlien
from .objects.WaterTerminal import WaterTerminal
from .objects.LazerControler import LazerControler

GAME_INTRO = "intro"
GAME_MAIN = "main"

game_state = GAME_INTRO

def intro_screen(clock):
    pygame.mixer.music.load("./assets/sounds/Intro_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) #loop


    font_big = TITLE_FONT
    font_small = START_FONT

    bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

    title = font_big.render("VIRUS GAME LOL", True, (200, 50, 200)) #Farge
    prompt = font_small.render("Press any key to start", True, (255, 255, 255))

    alpha = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.stop() #stop når spillet starter
                return
            
        if alpha < 255:
            alpha += 3
            title.set_alpha(alpha)

        screen.blit(bg_image, (0, 0))
        
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2-60)))
        screen.blit(prompt, prompt.get_rect(center =(WIDTH // 2, HEIGHT // 2+40)))

        pygame.display.flip()
        clock.tick(60)
                        

def run():
    pygame.display.set_caption("Virus game (First draft)")

    # Clock and timing
    clock = pygame.time.Clock()

    dt = 0
    last_virus_growth = 0

    intro_screen(clock)

    pygame.mixer.music.load("./assets/sounds/Ingame_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    #Sound effects
    shot_sound = pygame.mixer.Sound("./assets/sounds/Raygun_sound.mp3")
    shot_sound.set_volume(0.5)

    

    # Game objects
    p1 = Player()
    virus_growing_msg = OverlayMessage("The virus is growing", 250)
    virus_growth_overlay = VirusGrowthOverlay()
    inventory_display = InventoryDisplay()
    projectiles = []
    boulders = []

    enemies = pygame.sprite.Group()
    alien_invasion_happened = False

    door_requires_plate = True
    all_required_plates_active = False
    plates_pressed_correctly = []
    
    typing_task_completed = False
    pressure_plate_puzzle_complete = False


    ROOMS = {
        CONTROL_ROOM_NAME: ControlRoom(),
        MAIN_ROOM_NAME: MainRoom(),
        BATH_ROOM_NAME: BathRoom(),
        GROWTH_ROOM_NAME: GrowthRoom(),
        AIRLOCK_ROOM_NAME: AirlockRoom(),
        LABORATORY_ROOM_NAME: LaboratoryRoom()
    }
    current_room: Room = ROOMS[MAIN_ROOM_NAME]

    # Game states
    GAME_MAIN = "main"
    GAME_TYPING = "typing_minigame"
    game_state = GAME_MAIN


    def draw_frame():
        screen.blit(current_room.background, (0, 0))

        # Draws all room content
        current_room.draw_content(screen)

        # Projectiles
        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)

        # Enemy
        for alien in enemies:
            alien.draw(screen)
            alien.draw_healthbar(screen)

        # Player og healthbar
        p1.draw(screen)
        p1.draw_healthbar(screen)

        # Show inventory
        inventory_display.draw(screen, p1.inventory)

        # Purple Virus growth overlay
        virus_growth_overlay.draw(screen)
        if virus_growing_msg.show:
            virus_growing_msg.draw(screen)

        pygame.display.flip()


    def open_rocket_minigame():
        pygame.display.set_caption("Rocket Minigame")
        completed = run_rocket_game(screen)
        pygame.display.set_caption("Virus game (First draft)")
        return completed

    def open_typing_minigame():
        pygame.display.set_caption("Typing Minigame")
        completed = run_typing_game(screen)
        pygame.display.set_caption("Virus game (First draft)")
        return completed


    running = True
    while running:
        clock.tick(FRAMERATE) # Limit framerate
        current_time = pygame.time.get_ticks()
        player_can_press = None

        # Remove player tips
        if p1.tip_text is not None and current_time - p1.tip_displayed_time >= PLAYER_TIP_SHOW_TIME_MS:
            p1.remove_text_tip()

        # Virus growth
        if current_time - last_virus_growth >= VIRUS_GROWTH_COOLDOWN_MS:
            last_virus_growth = current_time
            p1.virus_growth += 1
            virus_growth_overlay.increse_alpha(p1.virus_growth)
            virus_growing_msg.show = True

            CagedAlien.instance.grow(p1.virus_growth)
        elif virus_growing_msg.show and current_time - last_virus_growth >= VIRUS_GROWTH_DISPLAY_MSG_TIME_MS:
            virus_growing_msg.show = False

        # Game end condition
        if p1.virus_growth >= VIRUS_GROWTH_KILL:
            running = False  # TODO: Replace with game end screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()

        # Move player
        v = [0, 0]
        if keys[pygame.K_a] and p1.x > 0: v[0] -= 1
        if keys[pygame.K_d] and p1.x < WIDTH - p1.size[0]: v[0] += 1
        if keys[pygame.K_w] and p1.y > 0: v[1] -= 1
        if keys[pygame.K_s] and p1.y < HEIGHT - p1.size[1]: v[1] += 1
        p1.move(v, dt)

        # Pressure plates
        player_stands_on_plate = False
        player_rect = pygame.Rect(p1.x, p1.y, p1.size[0], p1.size[1])
        for plate in PressurePlate.all_pressure_plates:
            if plate[1] == current_room.name and player_rect.colliderect(plate[0].rect):
                player_stands_on_plate = True
                plate[0].activate()

                if plate[0].text in PLATE_UNLOCK_COMBINATION and not plate[0] in plates_pressed_correctly: plates_pressed_correctly.append(plate[0])
        
        # Handle pressure plate puzzle
        if len(plates_pressed_correctly) >= 5 and not player_stands_on_plate:
            is_correct = True
            for i in range(len(plates_pressed_correctly)):
                if plates_pressed_correctly[i].text != PLATE_UNLOCK_COMBINATION[i]:
                    is_correct = False
                    break
            if not is_correct:
                for p in plates_pressed_correctly:
                    p.deactivate()
                plates_pressed_correctly = []
            else:
                pressure_plate_puzzle_complete = True
        
        # Ginger plant
        for plant_tuple in GingerPlant.all:
            if plant_tuple[1] != current_room.name: continue # Skip plants that are not in this room
    
            plant = plant_tuple[0]
            if typing_task_completed and not plant.grown:
                plant.grow()
            if plant.can_take(p1.x, p1.y, p1.size) and p1.can_interact(current_time):
                player_can_press = "E"
                if keys[pygame.K_e]:
                    p1.last_interaction = current_time
                    p1.collect(plant.take()) # Add ginger to player inventory
        
        # Tooth-paste safe
        for safe_tuple in Safe.all:
            if safe_tuple[1] != current_room.name: continue # Skip safes that are not in this room

            safe: Safe = safe_tuple[0]
            if pressure_plate_puzzle_complete and safe.locked:
                safe.open()
            if safe.can_take(p1.x, p1.y, p1.size) and p1.can_interact(current_time):
                player_can_press = "E"
                if keys[pygame.K_e]:
                    p1.last_interaction = current_time
                    p1.collect(safe.take_content()) # Add tooth paste to player inventory
        
        # Lab table
        for lab_table_tuple in LabTable.all:
            if lab_table_tuple[1] != current_room.name: continue # Skip safes that are not in this room

            lab_table: LabTable = lab_table_tuple[0]
            if lab_table.can_interact(p1.x, p1.y, p1.size) and p1.can_interact(current_time):
                player_can_press = "E"
                if keys[pygame.K_e]:
                    p1.last_interaction = current_time
                    cure_created = lab_table.make_cure(p1) # Make cure if you can
                    if not cure_created:
                        p1.add_timed_text_tip("Im missing some ingredients", current_time)

        # Handle doors
        door = current_room.open_door(p1.x, p1.y, p1.size)
        if door != "" and p1.can_interact(current_time):
            player_can_press = "E"
            if keys[pygame.K_e]:
                if len(enemies) <= 0:
                    p1.last_interaction = current_time # Update last interaction so player does not enter doors right after exiting
                    last_room = current_room.name
                    current_room = ROOMS[door]
                    enter_cords = current_room.get_enter_coords_from(last_room)
                    p1.go_to(enter_cords)
                else:
                    p1.add_timed_text_tip("I cannot let the invasion enter the ship", current_time)

        # Enemy aliens
        enemies.update(player_rect, dt)

        for enemy in enemies:
            if enemy.rect.colliderect(player_rect):
                if current_time - p1.last_hit_time >= p1.hit_cooldown:
                    p1.take_damage(10)
                    p1.last_hit_time = current_time

        if p1.health <= 0:
            print("Player died")
            running = False
        
        # Shoot aliens
        for projectile in projectiles[:]:
            projectile.update(dt)

            for alien in enemies:
                if projectile.rect.colliderect(alien.rect):
                    alien.take_damage(10)
                    projectiles.remove(projectile)
                
                    if alien.health <= 0:
                        enemies.remove(alien)
                    break

        # Open minigames
        if current_room.name == AIRLOCK_ROOM_NAME and LazerControler.instance.can_interact(p1.x, p1.y, p1.size):
            player_can_press = "E"
            if keys[pygame.K_e]:
                if open_rocket_minigame(): 
                    LazerControler.instance.done = True
                    p1.collect(STAR_DUST)
        if current_room.name == GROWTH_ROOM_NAME and WaterTerminal.instance.can_interact(p1.x, p1.y, p1.size):
            player_can_press = "E"
            if keys[pygame.K_e]:
                if open_typing_minigame():
                    WaterTerminal.instance.activate()
                    typing_task_completed = True
        if not alien_invasion_happened and current_room.name == AIRLOCK_ROOM_NAME and p1.y >= HEIGHT//3: # Trigger invasion when player 1/3 down
            current_room.invade() # Change background
            alien_invasion_happened = True
            for i in range(5):
                enemies.add(InvadingAlien(WIDTH-250, HEIGHT-200, 300))
                

        # Shooting (if needed)
        if keys[pygame.K_SPACE]:
            if current_time - p1.last_shot_time >= BULLET_COOLDOWN_MS:
                p1.last_shot_time = current_time
                projectile = p1.shoot()
                projectiles.append(projectile)
                shot_sound.play()
        
        # Shaw what player can press
        p1.add_key_tip(player_can_press)

        # Draw main game frame
        draw_frame()

        dt = clock.tick(FRAMERATE) / 1000

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
