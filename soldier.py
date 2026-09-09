import pygame
import screen
import consts
import game_field


def soldier_starting_place():
    # creates the soldier's starting position in the top left corner
    starting_position = []

    for i in range(consts.SOLDIER_ROWS):
        row = []

        for j in range(consts.SOLDIER_COLS):
            row.append([i, j])

        starting_position.append(row)

    return starting_position


current_soldier_location = soldier_starting_place()

soldier = {
    "place": current_soldier_location,
    "night_look": False,
    "touched_a_mine": False,
    "touched_a_flag": False
}




def check_if_touched_a_mine(game_grid):
    feet = soldier["place"][consts.SOLDIER_ROWS - 1]

    for place in feet:
        row = place[0]
        col = place[1]

        if game_grid[row][col]["type"] == "mine":
            soldier["touched_a_mine"] = True
            return True

    return False


def check_if_touched_the_flag(game_grid):
    for row in range(consts.SOLDIER_BODY_ROWS):
        for place in soldier["place"][row]:
            place_row = place[0]
            place_col = place[1]

            if game_grid[place_row][place_col]["type"] == "flag":
                soldier["touched_a_flag"] = True
                return True

    return False