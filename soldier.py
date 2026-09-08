import pygame
import screen
import consts
import game_field
def soldier_starting_place():
    starting_position=[]
    for i in range (consts.SOLDIER_ROWS):
        row = []
        for j in range (consts.SOLDIER_COLS):
            row.append(j)
        starting_position.append(row)
    return starting_position

current_soldier_location = soldier_starting_place()
soldier = {"place": current_soldier_location, "night_look": False, "touched_a_mine": False, "touched_a_flag": False}

def is_box_in_current_place(box):
    for row_in_location in range (len(current_soldier_location)):
        for col_in_location in range (len(row_in_location)):
            if box["x_place"] == row_in_location and box["y_place"] == col_in_location:
                return True
    return False


def check_if_touched_a_mine ():
    game_grid = game_field.field_intialization()
    for rows in range (len(game_grid)):
        for box in range (len(rows)):
            if is_box_in_current_place(box):
                if box["type"] == "mine":
                    soldier["touched_a_mine"]=True









