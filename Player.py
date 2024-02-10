import pygame

class Player:
    def __init__(self) -> None:
        pass

    def movement(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Moved Left")
                if event.key == pygame.K_RIGHT:
                    print("Moved Right")
                if event.key == pygame.K_DOWN:
                    print("Moved down")
                if event.key == pygame.K_UP:
                    print("Moved up")



