#On importe les modules : Pygame , random , math , time
from importlib.metadata import pass_none
from inspect import Parameter
from random import choice

import pygame
import random
import math
import time
from pygame import KEYDOWN, FULLSCREEN ,colordict
from pygame.examples.cursors import image

pygame.init()
screen = pygame.display.set_mode((0,0),FULLSCREEN)
#Constants
WIDTH, HEIGHT = screen.get_size()
FPS = 240

font = pygame.font.SysFont("Times New Roman", 35)
big_font = pygame.font.SysFont("Times New Roman", 55,True)


# Screen + Backgrounds
bg = pygame.image.load("Assets/BG.jpg")
bg_nuke = pygame.image.load("Assets/BG_nuke.jpg")
bg_parameters= pygame.image.load("Assets/BG_parameters.jpg")

cursor_image0 = pygame.image.load('Assets/Cursors/cursor_0.png').convert_alpha()
cursor_image1 = pygame.image.load('Assets/Cursors/cursor_1.png').convert_alpha()
cursor_image2 = pygame.image.load('Assets/Cursors/cursor_2.png').convert_alpha()
cursor_image3 = pygame.image.load('Assets/Cursors/cursor_3.png').convert_alpha()
cursor0 = pygame.cursors.Cursor((38,38), cursor_image0)
cursor1 = pygame.cursors.Cursor((38,38), cursor_image1)
cursor2 = pygame.cursors.Cursor((120,120), cursor_image2)
cursor3 = pygame.cursors.Cursor((75,75), cursor_image3)
current_cursor = cursor0

cursor0_display= cursor_image0.get_rect(center=(WIDTH/2+450,HEIGHT/2-300))
cursor1_display= cursor_image1.get_rect(center=(WIDTH/2+600,HEIGHT/2-300))
cursor2_display= cursor_image2.get_rect(center=(WIDTH/2+450,HEIGHT/2+300))
cursor3_display= cursor_image3.get_rect(center=(WIDTH/2+600,HEIGHT/2+300))




pygame.display.set_caption("Aim Trainer")


# The Setup Variables
circles = []
score = 0
combo = 0
highest_combo = 0
start_time = time.time()
difficulty = None
parameter = False

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
button_parameters = pygame.Rect(WIDTH-230, HEIGHT-70, 200, 50)

def draw_menu():
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen,pygame.Color("green"), button_easy)
    pygame.draw.rect(screen,pygame.Color("blue"), button_normal)
    pygame.draw.rect(screen,pygame.Color("red"), button_hard)
    pygame.draw.rect(screen,pygame.Color('purple'),button_parameters)

    easy_text = font.render("Facile", True,pygame.Color("black"))
    normal_text = font.render("Normal", True, pygame.Color("black"))
    hard_text = font.render("Difficile", True, pygame.Color("black"))
    button_parameters_text = font.render("Paramètres", True, pygame.Color("black"))

    screen.blit(easy_text, (button_easy.x + 20, button_easy.y + 10))
    screen.blit(normal_text, (button_normal.x + 20, button_normal.y + 10))
    screen.blit(hard_text, (button_hard.x + 20, button_hard.y + 10))
    screen.blit(button_parameters_text, (button_parameters.x + 20, button_parameters.y + 10))
    pygame.display.flip()

def draw_parameter_menu():
    screen.blit(bg_parameters, (0, 0))
    text_cursor_choice = big_font.render("Choisisser le curseur qui vous convient le mieux en cliquant dessus",True,pygame.Color("black"))
    screen.blit(text_cursor_choice, (0,HEIGHT/2))
    screen.blit(cursor_image0,cursor0_display)
    screen.blit(cursor_image1, cursor1_display)
    screen.blit(cursor_image2, cursor2_display)
    screen.blit(cursor_image3, cursor3_display)
    pygame.display.flip()



def display_timer(start_ticks):

    elapsed_time_ms = pygame.time.get_ticks() - start_ticks
    elapsed_time_sec = elapsed_time_ms // 1000
    minutes = elapsed_time_sec // 60
    seconds = elapsed_time_sec % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, pygame.Color("white"))
    screen.blit(timer_surface, (WIDTH - 100, 10))


class Circle:
    def __init__(self, radius):
        self.x = random.randint(radius+100, WIDTH - radius -100)
        self.y = random.randint(radius+200, HEIGHT - radius)
        self.radius = radius
        self.spawn_time = time.time()

    def draw(self):
        pygame.draw.circle(screen,pygame.Color("black"), (self.x, self.y), self.radius, 7)

    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)
        return distance < self.radius


#Main Loop
running = True
clock = pygame.time.lock()
start_ticks = pygame.time.get_ticks()

while running:
    pygame.mouse.set_cursor(current_cursor)
    clock.tick(FPS)
    if difficulty is None and parameter is False:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):
                    difficulty = "facile"
                elif button_normal.collidepoint(event.pos):
                    difficulty = "normal"
                elif button_hard.collidepoint(event.pos):
                    difficulty = "difficile"
                elif button_parameters.collidepoint(event.pos):
                    parameter = True
                if difficulty:
                    CIRCLE_RADIUS, CIRCLE_LIFETIME, SPAWN_RATE = set_difficulty(difficulty)
                    start_time = time.time()
                    circles = []
                    score = 0
                    combo = 0
                    highest_combo = 0
                    start_ticks = pygame.time.get_ticks()
    elif parameter is True :
        draw_parameter_menu()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    parameter = False
                    draw_parameter_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor0_display.collidepoint(event.pos):
                    current_cursor = cursor0
                if cursor1_display.collidepoint(event.pos):
                    current_cursor = cursor1
                if cursor2_display.collidepoint(event.pos):
                    current_cursor = cursor2
                if cursor3_display.collidepoint(event.pos):
                    current_cursor = cursor3


    else:
        screen.blit(bg_nuke, (0, 0))
        if time.time() - start_time >= SPAWN_RATE:
            circles.append(Circle(CIRCLE_RADIUS))
            start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type  == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    draw_menu()
                    difficulty = None

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

        score_text = font.render(f"Score: {score}", True, pygame.Color("white"))
        combo_text = font.render(f"Combo: {combo}", True, pygame.Color("white"))
        highest_combo_text = font.render(f"Highest Combo: {highest_combo}", True, pygame.Color("white"))
        difficulty_text = font.render(f"Difficulté: {difficulty}", True, pygame.Color("white"))
        duration_of_the_round = font.render("Temps de la manche : 3min", True, pygame.Color("white"))

        screen.blit(score_text, (10, 10))
        screen.blit(combo_text, (10, 50))
        screen.blit(highest_combo_text, (10, 90))
        screen.blit(difficulty_text, (10, 130))
        screen.blit(duration_of_the_round, (10, 170))
        display_timer(start_ticks)
        pygame.display.flip()

pygame.quit()
