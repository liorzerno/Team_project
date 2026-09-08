import pygame
import consts
import random
import sys


pygame.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#background display
def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    create_bush(game_state["original_bush"])


#image display
def create_bush(grass_img):
    grass_screen = pygame.image.load('grass.png')
    grass_screen = pygame.transform.scale(grass_screen, consts.GRASS_SIZE)
    grass_rect=grass_screen.get_rect()
    grass_list=[]

    for i in range(consts.MINES_COUNT):
        X_location = random.randint(0, consts.WINDOW_WIDTH)
        Y_location = random.randint(0, consts.WINDOW_HEIGHT)
        grass_list.append((X_location,Y_location))


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(consts.BACKGROUND_COLOR)
        for i in grass_list:
            screen.blit(grass_screen,i,grass_rect)
        pygame.display.flip()

    #     x=random.randint(1,consts.WINDOW_WIDTH)
    #     y=random.randint(1,consts.WINDOW_HEIGHT)
    #     screen.blit(grass_screen,(x,y))
    #     pygame.display.flip()

