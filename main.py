import consts
import screen
import pygame
x = 0
y = 0
state = {
        "flag": screen.flag_display(consts.FLAG_IMG),
        "soldier": screen.soldier_display( x, y),
        "bush": screen.create_bush(consts.GRASS_IMG),
        "is_window_open": True,
        "state": consts.RUNNING_STATE,
        "soldier_moving": False
    }


def main():
    pygame.init()
    while state["is_window_open"]:
        screen.draw_game(state)

if __name__ == '__main__':
    main()

