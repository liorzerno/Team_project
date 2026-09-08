import consts
import screen
import pygame

state = {
        "original_bush": screen.create_bush(consts.GRASS_IMG),
        "is_window_open": True,
        "state": consts.RUNNING_STATE
    }
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    pygame.init()
    while state["is_window_open"]:
        screen.draw_game(state)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
