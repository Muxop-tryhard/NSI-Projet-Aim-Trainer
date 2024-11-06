import pygame
import sys
import time
from src.model import Display_menu,Game,SQL_data_retriving
from pygame import KEYDOWN, FULLSCREEN, Color

#On initialise Pygame
pygame.init()



screen = pygame.display.set_mode((0,0),FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

#Ce seront les variables qui nous permettent de vérifier sur quel page on se situe
difficulty = None
parameter = None
leaderbord = None

#On charge les fonds d'écrans que l'ont uttilisera
bg=pygame.image.load("Assets/BG.jpg")
bg_nuke = pygame.image.load("Assets/BG_nuke.jpg")

#On charge les images des curseurs
cursors_images = []
for i in range(4):
    cursors_images.append(pygame.image.load("Assets/Cursors/cursor_{}.png".format(i)).convert_alpha())

#On définnit la position du curseur au centre de chaque image
cursors = []
cursors.append(pygame.cursors.Cursor((38,38), cursors_images[0]))
cursors.append(pygame.cursors.Cursor((38,38), cursors_images[1]))
cursors.append(pygame.cursors.Cursor((120,120), cursors_images[2]))
cursors.append(pygame.cursors.Cursor((75,75), cursors_images[3]))

#On définit les positions d'affichages de chaque curseurs dans le menu paramètres
cursors_images_display=[]
cursors_images_display.append(cursors_images[0].get_rect(center=(WIDTH / 2 - 450, HEIGHT / 2 - 300)))
cursors_images_display.append(cursors_images[1].get_rect(center=(WIDTH / 2 + 450, HEIGHT / 2 - 300)))
cursors_images_display.append(cursors_images[2].get_rect(center=(WIDTH / 2 - 450, HEIGHT / 2 + 300)))
cursors_images_display.append(cursors_images[3].get_rect(center=(WIDTH / 2 + 450, HEIGHT / 2 + 300)))

#On définit le curseur par défaut
pygame.mouse.set_cursor(cursors[0])

#On définit le nom de l'onglet qui apparaitra dans la barre des taches
pygame.display.set_caption("Aim Trainer")

#On charge les fonts que l'ont uttilisera
font = pygame.font.SysFont("Times New Roman", 35)
big_font = pygame.font.SysFont("Times New Roman", 55,True)

#On instancie la classe Clock qui nous permetra notamment de gérer la fréquence d'affichage
clock = pygame.time.Clock()


#On instancie les classes qui nous permettrons de : 1-Afficher du contenu 2-Joueur au jeu
display_menu=Display_menu.DisplayMenu(screen, WIDTH,HEIGHT ,pygame,font,bg)
game_runer=Game.Game_Maker(pygame)

sql_manager=SQL_data_retriving.SQL_querys()
sql_manager.insert('Denis', 'Difficile', 32, 3000000)
top_10_leaderboard = sql_manager.get_first_ten()

# On lance la du jeu
while True:

    clock.tick(120) #Limite le nombre de FPS à 120 pour améliorer la fluide en gardant le même nombre de FPS constant

    if all(Variables is None for Variables in [difficulty,parameter,leaderbord]):

        display_menu.draw_main_menu()
        difficulty,parameter,leaderbord = display_menu.choose_difficulty(difficulty,parameter,leaderbord)

    if difficulty:

        game_runer.launch_game(screen,difficulty,HEIGHT, WIDTH,display_menu,bg_nuke)
        difficulty = None

    if parameter:

        display_menu.draw_parameter_menu(big_font, cursors_images, cursors_images_display)
        display_menu.choose_cursor(cursors, cursors_images_display)
        parameter = None

    if leaderbord:
        display_menu.draw_leaderboard_menu()

        leaderbord = None
sql_manager.deconection()
pygame.quit()
