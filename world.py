import pygame
from tile import Tile
from player import Player


world = [
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
width = 1200
height = len(world) * tile_size


class World:
    def __init__(self, level, surface) -> None:
        self.surface = surface
        self.level = level
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.offset = 0
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

    def scrollx(self):
        if self.player.sprite.rect.centerx < 200:
            self.offset = 5
            self.player.sprite.move_x = 0
            self.player.sprite.rect.centerx = 200
        elif self.player.sprite.rect.centerx > 1000:
            self.offset = -5
            self.player.sprite.move_x = 0
            self.player.sprite.rect.centerx = 1000
        else:
            self.offset = 0

    def draw(self) -> None:
        self.tiles.update(self.offset, 0)
        self.tiles.draw(self.surface)
        self.player.update()       
        self.scrollx()
        self.player.draw(self.surface)
