import pygame
from tile import Tile
from player import Player


level = [
    '                    ',
    '                    ',
    '                    ',
    '  .                 ',
    '  .                 ',
    '  .                 ',
    ' ....      .....    ',
    '                    ',
    '       P            ',
    '....................',
]

tile_size = 64
width = 1200
height = len(level) * tile_size


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

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.x_speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.sprite.rect):
                if player.x_speed < 0:
                    player.rect.left = sprite.rect.right
                elif player.x_speed > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        self.player.sprite.rect.y += self.player.sprite.y_speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.sprite.rect):
                if player.y_speed < 0:
                    player.y_speed = 0
                    player.rect.top = sprite.rect.bottom
                elif player.y_speed > 0:
                    player.rect.bottom = sprite.rect.top
                    player.y_speed = 0

    def scrollx(self):
        if self.player.sprite.rect.centerx < 200:
            self.offset = 8
            self.player.sprite.move_x = 0
            self.player.sprite.rect.centerx = 200
        elif self.player.sprite.rect.centerx > 1000:
            self.offset = -8
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

        self.horizontal_collision()
        self.vertical_collision()
