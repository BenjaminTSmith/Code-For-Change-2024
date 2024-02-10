import pygame, sys
from player import Player
from world import *
from tile import Tile
import game_menu


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
    screen.fill("black")
    world.draw()
    pygame.display.flip()
    clock.tick(60)

