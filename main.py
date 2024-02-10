import pygame
from Player import Player
from World import *
from Tile import Tile


pygame.init()
print("PyGame initialized")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

world = World(world, screen)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    screen.fill("black");
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
