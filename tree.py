import pygame
import time


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.image.load("path/to/image")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(bottomleft=pos)
        self.plant_time = time.time()


    def check_for_growth(self):
        now = time.time()
        if self.plant_time - now > 500:
            self.image = pygame.image.load("path/to/growth")
        if self.plant_time - now > 1000:
            self.image = pygame.image.load("path/to/growth")


    def update(self, *args, **kwargs):
        self.check_for_growth()

