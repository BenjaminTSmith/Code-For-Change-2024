import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def increase_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10)) 
