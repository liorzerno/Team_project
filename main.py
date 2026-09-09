import sys
from itertools import count

import consts
import screen
import pygame
import time
x = 0
y = 0
state = {
        "soldier": screen.soldier_display( x, y),
        "is_window_open": True,
        "state": consts.RUNNING_STATE,
        "soldier_moving": False
    }

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



if __name__ == '__main__':
    main()

