import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')


tile_size = 50

#загрузка изображения
bg_img = pygame.image.load('fon.jpg')

def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class World():
    def __init__(self, data):
        self.tile_list = []

        #загрузка изображений
        stone_img = pygame.image.load('stone.png')
        grass_img = pygame.image.load('spike.png')
        spike2_img = pygame.image.load('spike2.png')
        player_img = pygame.image.load('player.png')
        enemy_img = pygame.image.load('enemy.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(stone_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(spike2_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                #Место нахождения игрока и врага
                if tile == 4:
                    img = pygame.transform.scale(player_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(enemy_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 0],
[3, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[4, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 5, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world = World(world_data)

game = True
while game:

    screen.blit(bg_img, (0, 0))

    world.draw()

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()

pygame.quit()