import pygame, sys
from Player import Player
from World import *
from Tile import Tile


pygame.init()
print("PyGame initialized")

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Environemental GAME")

world = World(world, screen)
world.create_world()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
<<<<<<< HEAD
        # player.movement(event, 10,10)
=======
        player.movement(event)
>>>>>>> dc2efa91e1e0d37975772c88709765652250a39c
    screen.fill("black")
    world.draw()
    pygame.display.flip()
    clock.tick(60)

