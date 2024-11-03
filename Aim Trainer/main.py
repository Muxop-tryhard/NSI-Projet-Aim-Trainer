import pygame
import time
from src.model import Circle,Display_menu
from pygame import KEYDOWN,FULLSCREEN

pygame.init()

screen = pygame.display.set_mode((0,0),FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
FPS = 240

bg=pygame.image.load("Assets/BG.jpg")
bg_nuke = pygame.image.load("Assets/BG_nuke.jpg")
bg_parameters= pygame.image.load("Assets/BG_parameters.jpg")

font = pygame.font.SysFont("Times New Roman", 35)
big_font = pygame.font.SysFont("Times New Roman", 55,True)

cursors_images = []
for i in range(4):
    cursors_images.append(pygame.image.load("Assets/Cursors/cursor_{}.png".format(i)).convert_alpha())

cursors = []
cursors.append(pygame.cursors.Cursor((38,38), cursors_images[0]))
cursors.append(pygame.cursors.Cursor((38,38), cursors_images[1]))
cursors.append(pygame.cursors.Cursor((120,120), cursors_images[2]))
cursors.append(pygame.cursors.Cursor((75,75), cursors_images[3]))

#Set default cursor
pygame.mouse.set_cursor(cursors[0])

cursors_images_display=[]
cursors_images_display.append(cursors_images[0].get_rect(center=(WIDTH / 2 + 450, HEIGHT / 2 - 300)))
cursors_images_display.append(cursors_images[1].get_rect(center=(WIDTH / 2 + 600, HEIGHT / 2 - 300)))
cursors_images_display.append(cursors_images[2].get_rect(center=(WIDTH / 2 + 450, HEIGHT / 2 + 300)))
cursors_images_display.append(cursors_images[3].get_rect(center=(WIDTH / 2 + 600, HEIGHT / 2 + 300)))

button_easy = pygame.Rect(200, 200, 150, 50)
button_normal = pygame.Rect(200, 300, 150, 50)
button_hard = pygame.Rect(200, 400, 150, 50)
button_parameters = pygame.Rect(WIDTH - 230, HEIGHT - 70, 200, 50)

pygame.display.set_caption("Aim Trainer")

# The Setup Variables
circles = []
score = 0
combo = 0
highest_combo = 0
start_time = time.time()
difficulty = None
parameter = False


#A mettre dans game
def set_difficulty(difficulty):
    if difficulty == "facile":
        return 60, 3, 2
    elif difficulty == "normal":
        return 50, 2, 1.5
    elif difficulty == "difficile":
        return 40, 1, 1





#Main Loop
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

display_menu=Display_menu.DisplayMenu(screen, WIDTH,HEIGHT ,pygame,font,bg,start_ticks)

while running:

    clock.tick(FPS)
    if difficulty is None and parameter is False:
        display_menu.draw_main_menu()

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
        display_menu.draw_parameter_menu(bg_parameters,big_font,cursors_images,cursors_images_display)
        display_menu.choose_cursor(cursors,cursors_images_display)
        parameter =False

    else:
        screen.blit(bg_nuke, (0, 0))
        if time.time() - start_time >= SPAWN_RATE:
            circles.append(Circle.Circle(CIRCLE_RADIUS, HEIGHT, WIDTH))
            start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type  == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display_menu.draw_main_menu()
                    difficulty = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                hit = False
                for circle in circles:
                    if circle.is_clicked(event.pos):
                        circles.remove(circle)
                        combo += 1
                        score += 1 * combo
                        hit = True
                        break
                if not hit:
                    combo = 0

        for circle in circles:
            if time.time() - circle.spawn_time > CIRCLE_LIFETIME:
                circles.remove(circle)
                combo = 0
            else:
                circle.draw(screen)

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
        display_menu.draw_game_timer()
        pygame.display.flip()

pygame.quit()
