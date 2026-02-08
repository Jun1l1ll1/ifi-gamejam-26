import pygame
import random
from ..options import *

# Example gibberish sentences
SENTENCES = [
    "blargh zork fleep",
    "trizzy womp glarn",
    "quix flobber snark",
    "ploop dribble twang"
]

def run(screen):
    pygame.display.set_caption("'Typing' - minigame")

    # Hovering scale
    HOVER_SCALE = 0.85
    MINIGAME_WIDTH = int(WIDTH * HOVER_SCALE)
    MINIGAME_HEIGHT = int(HEIGHT * HOVER_SCALE)
    hover_x = (WIDTH - MINIGAME_WIDTH) // 2
    hover_y = (HEIGHT - MINIGAME_HEIGHT) // 2

    # Surface for minigame logic
    minigame_surface = pygame.Surface((WIDTH, HEIGHT))



    # Init
    clock = pygame.time.Clock()
    running = True
    failed = False

    # Pick a random sentence
    target_sentence = random.choice(SENTENCES)
    typed_text = ""
    feedback = ""

    # Font
    font = pygame.font.SysFont(None, 30)


    def draw_frame():
        
        minigame_surface.fill((40, 40, 50))


        # Draw target sentence
        target_label = font.render("Type this:", True, (255, 255, 255))
        minigame_surface.blit(target_label, (20, 20))

        sentence_surf = font.render(target_sentence, True, (200, 200, 255))
        minigame_surface.blit(sentence_surf, (20, 60))

        # Draw typed text
        typed_surf = font.render(typed_text, True, (255, 255, 100))
        minigame_surface.blit(typed_surf, (20, 120))

        # Draw feedback if any
        if feedback:
            feedback_surf = font.render(feedback, True, (100, 255, 100))
            minigame_surface.blit(feedback_surf, (20, 180))

        # Scale and draw hover
        scaled_surface = pygame.transform.smoothscale(minigame_surface, (MINIGAME_WIDTH, MINIGAME_HEIGHT))
        screen.blit(scaled_surface, (hover_x, hover_y))
        pygame.display.update()


   
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                failed = True   # mark as failure, do NOT quit Pygame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    failed = True   # mark as failure, do NOT quit Pygame
                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if typed_text.strip() == target_sentence:
                        feedback = "Task Complete."
                        draw_frame()  # Show feedback
                        pygame.time.delay(1000)
                        running = False
                        return True  # Task success
                    else:
                        feedback = "ERROR. Try again."
                        typed_text = ""
                else:
                    typed_text += event.unicode


        draw_frame()

    if failed:
        # Show a Game Over message on hover surface
        minigame_surface.fill((40, 40, 50))
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        sub_text = font.render("You failed the minigame", True, (255, 255, 255))

        minigame_surface.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 20))
        minigame_surface.blit(sub_text, (WIDTH//2 - sub_text.get_width()//2, HEIGHT//2 + 20))

        # Scale and hover
        scaled_surface = pygame.transform.smoothscale(minigame_surface, (MINIGAME_WIDTH, MINIGAME_HEIGHT))
        screen.blit(scaled_surface, (hover_x, hover_y))
        pygame.display.update()
        pygame.time.delay(1500)  # show message for 1.5 seconds


    return False


if __name__ == "__main__":
    run()
