import pygame
import time
import random
import math

class Circle:
    def __init__(self, radius,HEIGHT,WIDTH):
        self.x = random.randint(radius+100, WIDTH - radius -100)
        self.y = random.randint(radius+200, HEIGHT - radius)
        self.radius = radius
        self.spawn_time = time.time()

    def draw(self,screen):
        pygame.draw.circle(screen,pygame.Color("black"), (self.x, self.y), self.radius, 7)

    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)
        return distance < self.radius
