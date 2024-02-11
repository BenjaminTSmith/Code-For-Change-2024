import pygame
import time


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/environment/Sapling.png")
        self.image_growth1 = pygame.image.load("assets/environment/Tree Stage 1.png")
        self.image_growth2 = pygame.image.load("assets/environment/Tree Stage 2.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(midbottom=pos)
        self.plant_time = pygame.time.get_ticks()

    def check_for_growth(self):
        now = pygame.time.get_ticks()
        elapsed_time = now - self.plant_time 
        if elapsed_time > 1000:
            self.image = self.image_growth1
        if elapsed_time > 2000:
            self.image = self.image_growth2

    def update(self, *offsets, **_):
        self.check_for_growth()
        self.rect.x += offsets[0]

