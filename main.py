import sys
from itertools import count

import consts
import screen
import pygame
import time

from Team_project.consts import WHITE
from Team_project.screen import draw_game

x = 0
y = 0
state = {
        "soldier": screen.soldier_display( x, y),
        "is_window_open": True,
        "state": consts.RUNNING_STATE,
        "soldier_moving": False
    }
def put_mines_in_place(field_grid):
    #findes the start of the mine
    # returns a list of where the image needs to be inserted
    insert_image=[]
    for rows in range (consts.BOARD_ROWS - 1):
        for col in range (consts.BOARD_COLS - 3):
            if field_grid[rows][col]["type"] == "mine" and field_grid[rows][col+1]["type"] == "mine" and field_grid[rows][col+2]["type"] == "mine":
                insert_image.append([rows,col])
    return insert_image


def main():
    pygame.init()
    screen.draw_game(state)

    while state["is_window_open"]:
        handle_user_events()

def handle_user_events():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.draw_night_mode()
                time.sleep(1)
                screen.draw_game(state)
                print("here")




if __name__ == '__main__':
    main()

