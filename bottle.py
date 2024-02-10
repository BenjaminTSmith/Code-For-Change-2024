import pygame

class Bottle:
    def __init__(self, pos):
        self.image = pygame.image.load("path/to/image")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(midbottom=pos)
        self.destroyed = False

    def hit(self, lumberjack):
        
        pass

    def is_destroyed(self):
        return self.destroyed

