import pygame
from Tile import Tile
from Player import Player


world = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    ' ....      .....    ',
    '                    ',
    '       P            ',
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
        self.player = pygame.sprite.GroupSingle()
        self.create_world()

    def create_world(self) -> None:
        for index, row in enumerate(self.level):
            for cell_index, cell in enumerate(row):
                x_pos = cell_index * tile_size
                y_pos = index * tile_size
                match cell:
                    case '.':
                        tile = Tile((x_pos, y_pos), tile_size)
                        self.tiles.add(tile)
                    case 'P':
                        player = Player((x_pos, y_pos))
                        self.player.add(player)

    def draw(self) -> None:
        self.tiles.update(0, 0)
        self.tiles.draw(self.surface)
        
        self.player.draw(self.surface)

