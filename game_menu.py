import pygame
import sys 

pygame.init()
res = (1280,640)

screen = pygame.display.set_mode(res)

def draw():

    color = (255,255,255)
    color_dark = (105, 105, 105)

    width = screen.get_width()
    height = screen.get_height()

    font = pygame.font.SysFont('Corbel', 105)
    smallfont = pygame.font.SysFont('Corbel', 35)
    start_text = font.render('Start', True, color)
    options_text = smallfont.render("Settings", True, color_dark)


    screen.blit(start_text, start_text.get_rect(center = screen.get_rect().center))
    screen.blit(options_text, (580, 380))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    screen.fill((69, 75, 27))

    mouse = pygame.mouse.get_pos()

    draw()
    pygame.display.update()