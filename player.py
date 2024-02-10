import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 64))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.move_x = 0 
        self.move_y = 0 
        self.accer = 0
        self.brake = 0
        self.vel = 5

    def movement(self): #make accerlation and brake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move_x = self.vel
        elif keys[pygame.K_LEFT]:
            self.move_x = -self.vel
        else:
            self.move_x = 0

            '''if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_x = -self.vel
                    print("moved left: ", self.move_x)
                if event.key == pygame.K_RIGHT:
                    self.move_x = self.vel
                    print("moved right: ",self.move_x)
                if event.key == pygame.K_DOWN:
                    self.move_y = self.vel
                    print("moved down: ", self.move_y)
                if event.key == pygame.K_UP:
                    self.move_y = -self.vel
                    print("moved up: ", self.move_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_x = 0
                if event.key == pygame.K_RIGHT:
                    self.move_x = 0
                if event.key == pygame.K_DOWN:
                    self.move_y = 0
                if event.key == pygame.K_UP:
                    self.move_y += 0'''

    def update(self, *args, **kwargs):
        self.movement()
        self.rect.x += self.move_x
        self.rect.y += self.move_y

                    



