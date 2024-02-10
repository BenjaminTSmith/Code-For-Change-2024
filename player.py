import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 64))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.x_speed = 0 
        self.y_speed = 0 
        self.gravity = 0.8
        self.jump_force = -16

    def movement(self): #make accerlation and brake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_speed = 8
        elif keys[pygame.K_LEFT]:
            self.x_speed = -8
        elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.y_speed = self.jump_force
        else:
            self.x_speed = 0

    def apply_physics(self):
        self.y_speed += self.gravity
        self.y_speed = min(16, self.y_speed)

    def update(self, *args, **kwargs):
        self.movement()
        self.apply_physics()

                    



