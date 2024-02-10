import pygame
import Player


pygame.init()
print("PyGame initialized")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        #Player.movement()

    screen.fill("black");
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
