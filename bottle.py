import pygame

class Bottle:
    def __init__(self, pos):
        self.image = pygame.image.load("path/to/image")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(midbottom=pos)
        self.destroyed = False

    def hit(self, lumberjack):
        if self.lumberjack_close(lumberjack):
            self.destroyed = True
            return True
        return False

    def lumberjack_close(self, lumberjack):
        if abs(lumberjack.rect.x - self.rect.x) < 10:
            if abs(lumberjack.rect.y - self.rect.y) < 10:
                return True
        return False

    def is_destroyed(self):
        return self.destroyed

