import pygame
from Tile import Tile


world = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    ' ....      .....    ',
    '                    ',
    'P                   ',
    '....................',
]

tile_size = 64
width = len(world[0]) * tile_size
height = len(world) * tile_size


class World:
    def __init__(self, level, surface) -> None:
        self.surface = surface
        self.level = level
        self.tiles = pygame.sprite.Group()
        self.create_world()

    def create_world(self) -> None:
        for index, row in enumerate(self.level):
            for cell_index, cell in enumerate(row):
                match cell:
                    case '.':
                        x_pos = cell_index * tile_size
                        y_pos = index * tile_size
                        tile = Tile((x_pos, y_pos), tile_size)
                        self.tiles.add(tile)
                    case 'P':
                        ...

    def draw(self) -> None:
        self.tiles.update(-3)
        self.tiles.draw(self.surface)

