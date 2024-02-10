import pygame, sys
from world import *
import game_menu
from score import Scoreboard

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Environemental Game")

world = World(level, screen)
world.create_world()
scoreboard = Scoreboard()
scoreboard.increase_score(10)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((135, 206, 235))
    world.draw()
    scoreboard.draw(screen)
    pygame.display.flip()
    clock.tick(60)

