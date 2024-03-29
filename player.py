import pygame
from animation import import_animations

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # setup
        self.animation_path = "assets/lumberjack"
        self.animations = {'idle' : [], 'run' : [], "chopping": []}
        for key in self.animations.keys():
            self.animations[key] = import_animations(self.animation_path + '/' + key)
        pygame.sprite.Sprite.__init__(self)
        self.image = self.animations['idle'][0]
        self.rect = self.image.get_rect(bottomleft=pos)

        # animation place holders
        self.idle = 0
        self.run = 0
        self.chopping = 0
        self.chopping = 0
        self.animation_speed = 0.15
        self.is_chopping = False

        #self.animations['chopping'][self.chopping]

        # movement settings
        self.x_speed = 0 
        self.y_speed = 0 
        self.gravity = 0.8
        self.jump_force = -18

    def animate_run(self, direction):
        if direction == "chopping":
            if int(self.chopping) >= len(self.animations["chopping"]):
                self.chopping = 0
            self.image = self.animations["chopping"][int(self.chopping)]
        if direction == "left":
            self.run += self.animation_speed
            if self.run > 7:
                self.run = 0
            self.image = self.animations['run'][int(self.run)]
        else:
            self.run += self.animation_speed
            if self.run > 15 or self.run < 8:
                self.run = 8
            self.image = self.animations['run'][int(self.run)]

    def movement(self):
        self.x_speed = 0
        self.image = self.animations['idle'][self.idle]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.is_chopping = False
            self.x_speed = 8
            self.animate_run("right")
            self.idle = 1
        elif keys[pygame.K_LEFT]:
            self.is_chopping = False
            self.x_speed = -8
            self.animate_run("left")
            self.idle = 0
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.is_chopping = False
            if self.y_speed == 0:
                self.y_speed = self.jump_force
        if keys[pygame.K_x]:
            self.is_chopping = True
            self.y_speed = 0
            self.x_speed = 0
            self.animate_run("chopping")
        

    def apply_physics(self):
        self.y_speed += self.gravity
        self.y_speed = min(16, self.y_speed)

    def update(self, *args, **kwargs):
        self.movement()
        self.apply_physics()

                    



