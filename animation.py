from os import walk
import pygame

def import_animations(filepath):
    surfaces = []
    for _, __, images in walk(filepath):
        for image in images:
            path = filepath + '/' + image
            image_surface = pygame.image.load(path).convert_alpha()
            image_surface = pygame.transform.scale(image_surface, (128, 187))
            surfaces.append(image_surface)

    return surfaces

