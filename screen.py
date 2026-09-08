import pygame
import consts
import random
import sys


pygame.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#drawing the whole game
def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    create_bush(game_state["bush"])
    soldier_display(game_state["soldier"])
    draw_message()
    drawGrid()
    flag_display(game_state["flag"])
    pygame.display.flip()

#bush display randomly
def create_bush(grass_img):
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
def flag_display(flag_img):
    screen.fill(consts.BACKGROUND_COLOR)
    flag_screen = pygame.image.load('flag.png')
    flag_screen = pygame.transform.scale(flag_screen, consts.FLAG_SIZE)
    screen.blit(flag_screen, (900,420,80,60))
    pygame.display.flip()

#display of soldier
def soldier_display(soldier_img):
    soldier_screen = pygame.image.load('soldier.png')
    soldier_screen = pygame.transform.scale(soldier_screen, consts.SOLDIER_SIZE)
    soldier_rect = soldier_screen.get_rect()
    screen.blit(soldier_screen, soldier_rect)
    pygame.display.flip()

#welcome text
def draw_message():
    font = pygame.font.SysFont(consts.FONT_NAME, consts.WELCOME_FONT_SIZE)
    text_img = font.render(consts.WELCOME_MESSAGE, True, consts.WHITE)
    text_rect = text_img.get_rect()
    screen.blit(text_img, text_rect)
    pygame.display.flip()

#enter mode
def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)





