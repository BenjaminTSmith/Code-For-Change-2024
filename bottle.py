import pygame

class Bottle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/environment/Plastic Bottle.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(midbottom=pos)
        self.destroyed = False

    def hit(self, lumberjack):
        if self.lumberjack_close(lumberjack):
            self.destroyed = True
            return True
        return False

    def lumberjack_close(self, lumberjack):
        if abs(lumberjack.rect.centerx - self.rect.centerx) < 100:
            if abs(lumberjack.rect.centery - self.rect.centery) < 100:
                return True
        return False

    def is_destroyed(self):
        return self.destroyed

    def update(self, *offsets, **kwargs):
        self.rect.x += offsets[0]

