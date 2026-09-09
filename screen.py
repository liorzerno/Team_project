import pygame
from pygame import image

import consts
import random
import sys

pygame.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#drawing the whole game
def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_message(consts.WELCOME_MESSAGE, consts.WELCOME_COLOR, consts.WELCOME_FONT_SIZE)
    soldier_display(0, 0)
    flag_display()
    create_bush()
    pygame.display.update()
    # drawGrid()


    pygame.display.flip()
def draw_night_mode():
    draw_grid()
    soldier_night_display(0, 0)
    pygame.display.flip()

def draw_grid():
    block_size = 20
    screen.fill(consts.BLACK)
    for x in range(block_size, consts.WINDOW_WIDTH, block_size):
        pygame.draw.line(screen, consts.BLOCK_COLOR, (x, 0), (x, consts.WINDOW_HEIGHT))

    for y in range(block_size, consts.WINDOW_HEIGHT, block_size):
        pygame.draw.line(screen, consts.BLOCK_COLOR, (0, y), (consts.WINDOW_WIDTH, y))


#bush display randomly
def create_bush():
    grass_screen = pygame.image.load('grass.png')
    grass_screen = pygame.transform.scale(grass_screen, consts.GRASS_SIZE)
    grass_rect=grass_screen.get_rect()
    grass_list=[]

    for i in range(consts.MINES_COUNT):
        x_location = random.randint(0, consts.WINDOW_WIDTH-30)
        y_location = random.randint(0, consts.WINDOW_HEIGHT-30)
        grass_list.append((x_location,y_location))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for i in grass_list:
            screen.blit(grass_screen,i,grass_rect)
        pygame.display.flip()

#display of flag
def flag_display():
    #screen.fill(consts.BACKGROUND_COLOR)
    flag_screen = pygame.image.load('flag.png')
    flag_screen = pygame.transform.scale(flag_screen, consts.FLAG_SIZE)
    screen.blit(flag_screen, (900,420,80,60))

#display of soldier
def soldier_display( x, y):
    soldier_screen = pygame.image.load('soldier.png')
    soldier_screen = pygame.transform.scale(soldier_screen, consts.SOLDIER_SIZE)
    soldier_rect = soldier_screen.get_rect()
    screen.blit(soldier_screen, soldier_rect)

def soldier_night_display( x, y):
    soldier_screen = pygame.image.load('soldier_night.png')
    soldier_screen = pygame.transform.scale(soldier_screen, consts.SOLDIER_SIZE)
    soldier_rect = soldier_screen.get_rect()
    screen.blit(soldier_screen, soldier_rect)

#welcome text
def draw_message(message, color, font_size):
    global screen
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_surface = font.render(message,True, color)
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, text_rect)






