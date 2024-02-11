import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/environment/dirt.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, *offsets, **_):
        self.rect.x += offsets[0]
