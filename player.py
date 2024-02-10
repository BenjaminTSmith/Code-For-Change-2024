import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 64))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.x_speed = 0 
        self.y_speed = 0 
        self.gravity = 0.08

    def movement(self): #make accerlation and brake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_speed = 5
        elif keys[pygame.K_LEFT]:
            self.x_speed = -5
        else:
            self.x_speed = 0

    def apply_physics(self):
        self.y_speed += self.gravity

    def update(self, *args, **kwargs):
        self.movement()
        self.apply_physics()
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

                    



