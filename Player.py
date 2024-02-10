import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0 
        self.move_y = 0 

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Moved Left")
                if event.key == pygame.K_RIGHT:
                    print("Moved Right")
                if event.key == pygame.K_DOWN:
                    print("Moved down")
                if event.key == pygame.K_UP:
                    print("Moved up")



