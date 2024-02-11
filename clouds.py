import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def create_clouds(num_clouds):
    cloud_images = [
    "assets/environment/small cloud 1.png",
    "assets/environment/small cloud 2.png",
    "assets/environment/big cloud 1.png",
    "assets/environment/big cloud 2.png"
    ]
    clouds = pygame.sprite.Group()
    for i in range(num_clouds):
        x = random.randint(0, 1200)  # Adjust as needed based on your screen width
        y = random.randint(0, 100)   # Adjust as needed based on your screen height
        image_path = random.choice(cloud_images)
        cloud = Cloud(x, y, image_path)
        clouds.add(cloud)
    return clouds

