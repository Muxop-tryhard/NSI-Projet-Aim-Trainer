import pygame
import random
import math
import time
from pygame import KEYDOWN, FULLSCREEN

pygame.init()

#Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 240
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
font = pygame.font.SysFont("Times New Roman", 35)


# Screen + Backgrounds
bg = pygame.image.load("Assets/BG.jpg")
bg_nuke = pygame.image.load(("Assets/BG_nuke.jpg"))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Aim Trainer")


# The Setup Variables
circles = []
score = 0
combo = 0
highest_combo = 0
start_time = time.time()
difficulty = None

def set_difficulty(difficulty):
    if difficulty == "facile":
        return 60, 3, 2
    elif difficulty == "normal":
        return 50, 2, 1.5
    elif difficulty == "difficile":
        return 40, 1, 1


# Main menu
button_easy = pygame.Rect(200, 200, 150, 50)
button_normal = pygame.Rect(200, 300, 150, 50)
button_hard = pygame.Rect(200, 400, 150, 50)

def draw_menu():
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, GREEN, button_easy)
    pygame.draw.rect(screen, BLUE, button_normal)
    pygame.draw.rect(screen, RED, button_hard)

    easy_text = font.render("Facile", True, BLACK)
    normal_text = font.render("Normal", True, BLACK)
    hard_text = font.render("Difficile", True, BLACK)

    screen.blit(easy_text, (button_easy.x + 20, button_easy.y + 10))
    screen.blit(normal_text, (button_normal.x + 20, button_normal.y + 10))
    screen.blit(hard_text, (button_hard.x + 20, button_hard.y + 10))
    pygame.display.flip()

def display_timer(start_ticks):
    elapsed_time_ms = pygame.time.get_ticks() - start_ticks
    elapsed_time_sec = elapsed_time_ms // 1000
    minutes = elapsed_time_sec // 60
    seconds = elapsed_time_sec % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, WHITE)
    screen.blit(timer_surface, (WIDTH - 100, 10))

class Circle:
    def __init__(self, radius):
        self.x = random.randint(radius, WIDTH - radius)
        self.y = random.randint(radius, HEIGHT - radius)
        self.radius = radius
        self.spawn_time = time.time()

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius, 15)

    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)
        return distance < self.radius

#Main Loop
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

while running:
    clock.tick(FPS)
    if difficulty is None:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):
                    difficulty = "facile"
                elif button_normal.collidepoint(event.pos):
                    difficulty = "normal"
                elif button_hard.collidepoint(event.pos):
                    difficulty = "difficile"

                if difficulty:
                    CIRCLE_RADIUS, CIRCLE_LIFETIME, SPAWN_RATE = set_difficulty(difficulty)
                    start_time = time.time()
                    circles = []
                    score = 0
                    combo = 0
                    highest_combo = 0
                    start_ticks = pygame.time.get_ticks()
    else:
        screen.fill(BLACK)
        screen.blit(bg_nuke, (0, 0))

        if time.time() - start_time >= SPAWN_RATE:
            circles.append(Circle(CIRCLE_RADIUS))
            start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type  == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                hit = False
                for circle in circles:
                    if circle.is_clicked(event.pos):
                        circles.remove(circle)
                        score += 1*combo
                        combo += 1
                        hit = True
                        break
                if not hit:
                    combo = 0

        for circle in circles:
            if time.time() - circle.spawn_time > CIRCLE_LIFETIME:
                circles.remove(circle)
                combo = 0
            else:
                circle.draw()

        if combo > highest_combo:
            highest_combo = combo

        score_text = font.render(f"Score: {score}", True, WHITE)
        combo_text = font.render(f"Combo: {combo}", True, WHITE)
        highest_combo_text = font.render(f"Highest Combo: {highest_combo}", True, WHITE)
        difficulty_text = font.render(f"Difficulté: {difficulty.capitalize()}", True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(combo_text, (10, 50))
        screen.blit(highest_combo_text, (10, 90))
        screen.blit(difficulty_text, (10, 130))

        display_timer(start_ticks)
        pygame.display.flip()

pygame.quit()
