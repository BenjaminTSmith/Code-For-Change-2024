import pygame, sys
from world import *
import game_menu

game_menu.main_menu()

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Environemental Game")

world = World(level, screen)
world.create_world()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("blue")
    world.draw()
    pygame.display.flip()
    clock.tick(60)

