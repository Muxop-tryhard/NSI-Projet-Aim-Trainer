
class DisplayMenu:

#mettre le BG dans le init

    def __init__(self,screen,WIDTH,HEIGHT,pygame,font):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.pygame = pygame
        self.font = font

    def draw_main_menu(self,bg):
        self.screen.blit(bg, (0, 0))

        button_easy = self.pygame.Rect(200, 200, 150, 50)
        button_normal = self.pygame.Rect(200, 300, 150, 50)
        button_hard = self.pygame.Rect(200, 400, 150, 50)
        button_parameters = self.pygame.Rect(self.WIDTH - 230, self.HEIGHT - 70, 200, 50)

        self.pygame.draw.rect(self.screen, self.pygame.Color("green"), button_easy)
        self.pygame.draw.rect(self.screen, self.pygame.Color("blue"), button_normal)
        self.pygame.draw.rect(self.screen, self.pygame.Color("red"), button_hard)
        self.pygame.draw.rect(self.screen, self.pygame.Color('purple'), button_parameters)

        easy_text = self.font.render("Facile", True, self.pygame.Color("black"))
        normal_text = self.font.render("Normal", True, self.pygame.Color("black"))
        hard_text = self.font.render("Difficile", True, self.pygame.Color("black"))
        button_parameters_text = self.font.render("Paramètres", True, self.pygame.Color("black"))

        self.screen.blit(easy_text, (button_easy.x + 20, button_easy.y + 10))
        self.screen.blit(normal_text, (button_normal.x + 20, button_normal.y + 10))
        self.screen.blit(hard_text, (button_hard.x + 20, button_hard.y + 10))
        self.screen.blit(button_parameters_text, (button_parameters.x + 20, button_parameters.y + 10))
        self.pygame.display.flip()

    def draw_parameter_menu(self,bg_parameters,big_font,cursors_images,cursors_display):
        self.screen.blit(bg_parameters, (0, 0))
        text_cursor_choice = big_font.render("Choisisser le curseur qui vous convient le mieux en cliquant dessus",
                                             True, self.pygame.Color("black"))
        self.screen.blit(text_cursor_choice, (0, self.HEIGHT / 2))
        self.screen.blit(cursors_images[3], cursors_display[3])
        self.screen.blit(cursors_images[0], cursors_display[0])
        self.screen.blit(cursors_images[1], cursors_display[1])
        self.screen.blit(cursors_images[2], cursors_display[2])
        self.pygame.display.flip()


    def launch_game(self):
        pass

    def choose_cursor(self,cursors,cursors_images_display,bg):
        exit = False
        while exit == False:
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_ESCAPE:
                        exit = True
                        self.draw_main_menu(bg)
                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    if cursors_images_display[0].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[0])
                    if cursors_images_display[1].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[1])
                    if cursors_images_display[2].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[2])
                    if cursors_images_display[3].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[3])
