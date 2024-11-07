import math
import random
import time

class Circle:

    def __init__(self, radius,HEIGHT,WIDTH,pygame):
        self.x = random.randint(radius+100, WIDTH - radius -100)
        self.y = random.randint(radius+200, HEIGHT - radius)
        self.radius = radius
        self.spawn_time = time.time()
        self.pygame = pygame

    def draw(self,screen):
        self.pygame.draw.circle(screen,self.pygame.Color("black"), (self.x, self.y), self.radius, 7)

    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)
        return distance < self.radius

class Game_Maker:

    def __init__(self,pygame,sql_manager):
        self.pygame=pygame
        self.sql_manager=sql_manager

    def set_difficulty(self,difficulty):

        if difficulty == "facile":
            return (60, 3, 2)
        elif difficulty == "normal":
            return (50, 2, 1.5)
        elif difficulty == "difficile":
            return (40, 1, 1)

    def launch_game(self,screen,difficulty,HEIGHT,WIDTH,display_menu,bg_nuke):

        circles = []
        CIRCLE_RADIUS, CIRCLE_LIFETIME, SPAWN_RATE = self.set_difficulty(difficulty)

        score = 0
        combo = 0
        highest_combo = 0

        last_spawn_time = time.time()
        start_ticks = self.pygame.time.get_ticks()
        starting_time = time.time()
        game_duration = 0

        while game_duration <= 5:
            game_duration =+ time.time() - starting_time
            display_menu.display_game_background(bg_nuke)

            if time.time() - last_spawn_time >= SPAWN_RATE:
                circles.append(Circle(CIRCLE_RADIUS, HEIGHT, WIDTH,self.pygame))
                last_spawn_time = time.time()

            for circle in circles:
                circle.draw(screen)

            for event in self.pygame.event.get():

                if event.type == self.pygame.KEYDOWN and event.key == self.pygame.K_ESCAPE:
                        return

                if event.type == self.pygame.MOUSEBUTTONDOWN:
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

            display_menu.draw_game_timer(start_ticks)
            display_menu.draw_relative_game_infos(score, combo, highest_combo, difficulty)
            self.pygame.display.flip()

        self.sql_manager.insert(difficulty,highest_combo,score)