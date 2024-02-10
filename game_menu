import pygame
import sys 

pygame.init()
res = (700,700)

screen = pygame.display.set_mode(res)

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Quit', True, color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 40:
                pygame.quit()
                sys.exit()
    
    screen.fill((60,25,60))

    mouse = pygame.mouse.get_pos()

    screen.blit(text, (width/2 + 50, height/2))
    pygame.display.update()