import pygame
import consts
import random


pygame.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#background display
def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    create_bush(game_state["original_bush"])


#image display
def create_bush(grass):
    grass_screen = pygame.image.load('grass.png')
    for i in range(consts.MINES_COUNT):
        x=random.randint(1,consts.WINDOW_WIDTH)
        y=random.randint(1,consts.WINDOW_HEIGHT)
        screen.blit(grass_screen,(x,y))
