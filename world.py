import pygame
import random
from tile import Tile
from player import Player
from bottle import Bottle
from tree import Tree
from score import Scoreboard


level = [
    '                                      ',
    '                                      ',
    '                                      ',
    '          ',
    '                      ',
    '',
    '                                      ',
    '                                      ',
    '       P                                   ',                 
    '............................................',
]

tile_size = 64
width = 1200
height = len(level) * tile_size


class World:
    def __init__(self, level, surface) -> None:
        self.surface = surface
        self.level = level
        self.tiles = pygame.sprite.Group()
        self.trees = pygame.sprite.Group()
        self.bottles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.offset = 0
        self.create_world()
        self.spawn_bottle()
        self.timer = pygame.time.get_ticks()

    def create_world(self) -> None:
        for index, row in enumerate(self.level):
            for cell_index, cell in enumerate(row):
                x_pos = cell_index * tile_size
                y_pos = index * tile_size
                match cell:
                    case '.':
                        tile = Tile((x_pos, y_pos))
                        self.tiles.add(tile)
                    case 'P':
                        player = Player((x_pos, y_pos))
                        self.player.add(player)

    def spawn_bottle(self):
        while True:
            print("spawning bottles")
            random_choice = random.randrange(0, len(self.level[-2]))
            if self.level[-2][random_choice] == ' ':
                self.bottles.add(Bottle((random_choice * 64, 576)))
                Scoreboard.decrease_score(10)
                break
            


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
            if sprite.rect.colliderect(player.rect):
                if player.y_speed < 0:
                    player.y_speed = 0.3
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

    def draw(self):
        
        if pygame.time.get_ticks() - self.timer > 8000:
            self.spawn_bottle()
            self.timer = pygame.time.get_ticks()

        self.player.update()       
        self.scrollx()
        self.player.draw(self.surface)

        self.tiles.update(self.offset)
        self.tiles.draw(self.surface)

        self.trees.update(self.offset)
        self.trees.draw(self.surface)
        if self.player.sprite.is_chopping:
            for bottle in self.bottles.sprites():
                if bottle.hit(self.player.sprite):
                    self.bottles.remove(bottle)
                    self.trees.add(Tree((bottle.rect.left, bottle.rect.bottom)))
        self.bottles.update(self.offset)
        self.bottles.draw(self.surface)

        self.horizontal_collision()
        self.vertical_collision()
'''
    def points(self, bottles):
        for bottle in self.bottles:
            if bottle.is_destroyed:
                increase_score(10)
            elif not bottle.is_destroyed:
                decrease_score(10)
            
        return points
 '''   