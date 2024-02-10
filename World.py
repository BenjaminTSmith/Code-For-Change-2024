import pygame
from Tile import Tile


world = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    'P                   ',
    '....................',
]

tile_size = 32
width = 1200
height = len(world) * tile_size

class World:
    def __init__(self, level, surface) -> None:
        self.surface = surface
        self.level = level
        for _ in level:
            pass


