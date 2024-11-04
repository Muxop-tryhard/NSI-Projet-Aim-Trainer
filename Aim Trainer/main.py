import pygame
#La bibliho
import time
from src.model import Display_menu,Game
from pygame import KEYDOWN, FULLSCREEN, Color

pygame.init()

difficulty = None
parameter = None

screen = pygame.display.set_mode((0,0),FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()


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

#Main Loop
running = True
clock = pygame.time.Clock() #On instancie la classe Clock qui nous permetra notamment de gérer la fréquence d'affichage


display_menu=Display_menu.DisplayMenu(screen, WIDTH,HEIGHT ,pygame,font,bg)
game_runer=Game.Game_maker(pygame)

while running:
    clock.tick(120) #Limite le nombre de FPS à 120 pour améliorer la fluide en gardant le même nombre de FPS constant

    if difficulty is None and parameter is None:
        start_ticks = pygame.time.get_ticks()
        display_menu.draw_main_menu()
        difficulty,parameter = display_menu.choose_difficulty(difficulty, parameter)

    if difficulty:
        game_runer.launch_game(screen,difficulty,HEIGHT, WIDTH,display_menu,bg_nuke)
        difficulty = None

    if parameter:
        display_menu.draw_parameter_menu(bg_parameters,big_font, cursors_images, cursors_images_display)
        display_menu.choose_cursor(cursors, cursors_images_display)
        parameter = None

pygame.quit()
