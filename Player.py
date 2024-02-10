import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0 
        self.move_y = 0 

    #def sprite(self):

    def movement(self, x, y):
        #create accerlation, velocity, brakes
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        
                        move_x -= x
                        print("Moved Left")
                    if event.key == pygame.K_RIGHT:
                        move_x += x
                        print("Moved Right")
                    if event.key == pygame.K_DOWN:
                        move_y -= y
                        print("Moved down")
                    if event.key == pygame.K_UP:
                        move_y += y
                        print("Moved up")
                

    def update(self):
        self.rect.x = self.rect.x + self.move.x



        
    
