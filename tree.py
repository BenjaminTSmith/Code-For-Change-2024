import pygame
import time


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/environment/Sapling.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(bottomleft=pos)
        self.plant_time = time.time()

    def check_for_growth(self):
        now = time.time()
        if self.plant_time - now > 1:
            self.image = pygame.image.load("assets/environment/Tree Growth 1.png")
        if self.plant_time - now > 2:
            self.image = pygame.image.load("assets/environment/Tree Growth 2.png")


    def update(self, *offsets, **_):
        self.check_for_growth()
        self.rect.x += offsets[0]

