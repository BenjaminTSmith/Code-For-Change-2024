import pygame, sys
from world import *
import game_menu
from score import Scoreboard
import animation
import clouds

print(animation.import_animations("assets/lumberjack/run"))


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Lumberjack's Revenge")
world = World(level, screen)
world.create_world()

cloud_group = clouds.create_clouds(8)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((135, 206, 235))
    cloud_group.draw(screen)
    world.draw()
    pygame.display.flip()
    clock.tick(60)

