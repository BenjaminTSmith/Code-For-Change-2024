import pygame
from animation import import_animations

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # setup
        self.animation_path = "assets/lumberjack"
        self.animations = {'idle' : [], 'run' : []}
        for key in self.animations.keys():
            self.animations[key] = import_animations(self.animation_path + '/' + key)

        pygame.sprite.Sprite.__init__(self)
        self.image = self.animations['idle'][0]
        self.rect = self.image.get_rect(topleft=pos)

        # animation place holders
        self.idle = 0
        self.run = 0
        self.chopping = 0

        # movement settings
        self.x_speed = 0 
        self.y_speed = 0 
        self.gravity = 0.8
        self.jump_force = -20


    def movement(self):
        self.x_speed = 0
        self.image = self.animations['idle'][self.idle]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_speed = 8
            self.image = self.animations['run'][self.run]
            self.run += 1
            self.idle = 0
        if keys[pygame.K_LEFT]:
            self.x_speed = -8
            self.image = self.animations['run'][self.run]
            self.run += 1
            self.idle = 1
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if self.y_speed == 0:
                self.y_speed = self.jump_force

    def apply_physics(self):
        self.y_speed += self.gravity
        self.y_speed = min(16, self.y_speed)

    def update(self, *args, **kwargs):
        self.movement()
        self.apply_physics()

                    



