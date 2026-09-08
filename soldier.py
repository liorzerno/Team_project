import pygame
import screen
import consts

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




