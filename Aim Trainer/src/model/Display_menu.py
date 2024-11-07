import sys

class DisplayMenu:

    def __init__(self,screen,WIDTH,HEIGHT,pygame,font,bg,sql_manager):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.pygame = pygame
        self.font = font
        self.bg = bg
        self.sql_manager = sql_manager

    def draw_main_menu(self):
        self.screen.blit(self.bg, (0, 0))

        button_easy = self.pygame.Rect(200, 200, 150, 50)
        button_normal = self.pygame.Rect(200, 300, 150, 50)
        button_hard = self.pygame.Rect(200, 400, 150, 50)
        button_parameters = self.pygame.Rect(self.WIDTH - 230, self.HEIGHT - 70, 200, 50)
        button_leaderboard = self.pygame.Rect(self.WIDTH - 230, self.HEIGHT - 140, 200, 50)

        self.pygame.draw.rect(self.screen, self.pygame.Color("green"), button_easy)
        self.pygame.draw.rect(self.screen, self.pygame.Color("blue"), button_normal)
        self.pygame.draw.rect(self.screen, self.pygame.Color("red"), button_hard)
        self.pygame.draw.rect(self.screen, self.pygame.Color('purple'), button_parameters)
        self.pygame.draw.rect(self.screen, self.pygame.Color('deeppink4'), button_leaderboard)

        easy_text = self.font.render("Facile", True, self.pygame.Color("black"))
        normal_text = self.font.render("Normal", True, self.pygame.Color("black"))
        hard_text = self.font.render("Difficile", True, self.pygame.Color("black"))
        button_parameters_text = self.font.render("Paramètres", True, self.pygame.Color("black"))
        button_leaderboard_text = self.font.render("Leaderboard", True, self.pygame.Color("black"))

        self.screen.blit(easy_text, (button_easy.x + 20, button_easy.y + 10))
        self.screen.blit(normal_text, (button_normal.x + 20, button_normal.y + 10))
        self.screen.blit(hard_text, (button_hard.x + 20, button_hard.y + 10))
        self.screen.blit(button_parameters_text, (button_parameters.x + 20, button_parameters.y + 10))
        self.screen.blit(button_leaderboard_text, (button_leaderboard.x + 10, button_leaderboard.y + 10))
        self.pygame.display.flip()

    def draw_parameter_menu(self,big_font,cursors_images,cursors_images_display):

        text_cursor_choice = big_font.render("Choisisser le curseur qui vous convient le mieux en cliquant dessus", True, self.pygame.Color("black"))

        self.screen.fill((self.pygame.Color("purple")))
        self.screen.blit(text_cursor_choice, (200, self.HEIGHT / 2))
        self.screen.blit(cursors_images[3], cursors_images_display[3])
        self.screen.blit(cursors_images[0], cursors_images_display[0])
        self.screen.blit(cursors_images[1], cursors_images_display[1])
        self.screen.blit(cursors_images[2], cursors_images_display[2])
        self.pygame.display.flip()

    def draw_leaderboard_menu(self):

        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN and event.key == self.pygame.K_ESCAPE:
                    return
            self.screen.fill((self.pygame.Color("deeppink4")))
            self.display_leaderboard_top_10(self.sql_manager.get_first_ten())
            self.pygame.display.flip()

    def choose_cursor(self,cursors,cursors_images_display):

        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN and event.key == self.pygame.K_ESCAPE:
                    return
                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    if cursors_images_display[0].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[0])
                    if cursors_images_display[1].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[1])
                    if cursors_images_display[2].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[2])
                    if cursors_images_display[3].collidepoint(event.pos):
                        self.pygame.mouse.set_cursor(cursors[3])

    def choose_difficulty(self,difficulty,parameter,leaderboard):

            for event in self.pygame.event.get():
                if event.type == self.pygame.KEYDOWN and event.key == self.pygame.K_ESCAPE:
                        self.pygame.quit()
                        sys.exit()
                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    if self.pygame.Rect(200, 200, 150, 50).collidepoint(event.pos):
                        difficulty = "facile"
                    elif self.pygame.Rect(200, 300, 150, 50).collidepoint(event.pos):
                        difficulty = "normal"
                    elif self.pygame.Rect(200, 400, 150, 50).collidepoint(event.pos):
                        difficulty = "difficile"
                    elif self.pygame.Rect(self.WIDTH - 230, self.HEIGHT - 70, 200, 50).collidepoint(event.pos):
                        parameter = True
                    elif self.pygame.Rect(self.WIDTH - 230, self.HEIGHT - 140, 200, 50).collidepoint(event.pos):
                        leaderboard = True
            return (difficulty,parameter,leaderboard)

    def draw_game_timer(self,start_ticks):

        elapsed_time_ms = self.pygame.time.get_ticks() - start_ticks
        elapsed_time_sec = elapsed_time_ms // 1000

        minutes = elapsed_time_sec // 60
        seconds = elapsed_time_sec % 60

        timer_text = f"{minutes:02}:{seconds:02}"
        timer_surface = self.font.render(timer_text, True, self.pygame.Color("white"))

        self.screen.blit(timer_surface, (self.WIDTH - 100, 10))

    def draw_relative_game_infos(self,score,combo,highest_combo,difficulty):

        score_text = self.font.render(f"Score: {score}", True, self.pygame.Color("white"))
        combo_text = self.font.render(f"Combo: {combo}", True, self.pygame.Color("white"))
        highest_combo_text = self.font.render(f"Highest Combo: {highest_combo}", True, self.pygame.Color("white"))
        difficulty_text = self.font.render(f"Difficulté: {difficulty}", True, self.pygame.Color("white"))
        duration_of_the_round_text = self.font.render("Temps de la manche : 3min", True, self.pygame.Color("white"))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(combo_text, (10, 50))
        self.screen.blit(highest_combo_text, (10, 90))
        self.screen.blit(difficulty_text, (10, 130))
        self.screen.blit(duration_of_the_round_text, (10, 170))
        self.pygame.display.flip()

    def display_game_background(self,bg_nuke):
        self.screen.blit(bg_nuke, (0, 0))

    def display_leaderboard_top_10(self,leaderboard_top_10):

        list_columns = ['Username','Difficulty','Highest Combo','Score']
        column_widths = [200, 200, 200, 225]
        for i, col in enumerate(list_columns):
            text = self.font.render(col, True, self.pygame.Color('black'))
            self.screen.blit(text, (500+column_widths[i] * i + 10,100))

        for i,value in enumerate(leaderboard_top_10):
            y_display_coordinate = 35 + (i + 1) * 45
            for j,text_info in enumerate(value):
                text = self.font.render(str(text_info), True,self.pygame.Color('black'))
                self.screen.blit(text, (500+column_widths[j] * j + 10, y_display_coordinate+100))
