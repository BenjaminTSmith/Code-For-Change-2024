import pygame
import animation

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # setup
        self.animation_path = "assets/lumberjack"
        self.images = animation.import_animations(self.animation_path)

        pygame.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)

        # movement settings
        self.x_speed = 0 
        self.y_speed = 0 
        self.gravity = 0.8
        self.jump_force = -20


    def movement(self):
        self.x_speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_speed = 8
            self.image = self.images[0]
        if keys[pygame.K_LEFT]:
            self.x_speed = -8
            self.image = self.images[1]
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if self.y_speed == 0:
                self.y_speed = self.jump_force

    def apply_physics(self):
        self.y_speed += self.gravity
        self.y_speed = min(16, self.y_speed)

    def update(self, *args, **kwargs):
        self.movement()
        self.apply_physics()

                    



