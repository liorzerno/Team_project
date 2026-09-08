import consts
import screen
import pygame

state = {
        "flag": screen.flag_display(consts.FLAG_IMG),
        "soldier": screen.soldier_display(consts.SOLDIER_IMG),
        "bush": screen.create_bush(consts.GRASS_IMG),
        "is_window_open": True,
        "state": consts.RUNNING_STATE
    }


def main():
    pygame.init()
    while state["is_window_open"]:
        screen.draw_game(state)

if __name__ == '__main__':
    main()

