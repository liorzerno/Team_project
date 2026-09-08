import pygame
import screen
import consts
import game_field


def soldier_starting_place():
    """creates a matrix for soldiers size and puts it top left corner"""
    starting_position = []
    for i in range(consts.SOLDIER_ROWS):
        row = []
        for j in range(consts.SOLDIER_COLS):
            row.append([i, j])
        starting_position.append(row)
    return starting_position

#puts the location at beginning
current_soldier_location = soldier_starting_place()
soldier = {"place": current_soldier_location, "night_look": False, "touched_a_mine": False, "touched_a_flag": False}

game_grid = game_field.field_initialization()


def check_if_touched_a_mine():
    """checks if in the row of the feet is a bomb"""
    for rows in range(len(game_grid)):
        for box in range(len(rows)):
            if ((soldier["place"][3] == box["x_place"] and soldier["place"][3][0] == box["y_place"]) or
                    (soldier["place"][3] == box["x_place"] and soldier["place"][3][1] == box["y_place"])):
                if box["type"] == "mine":
                    soldier["touched_a_mine"] = True


def check_if_touched_the_flag():
    """checks if the body of the soldier touches the flag"""
    game_grid = game_field.field_intialization()
    for rows in range(len(game_grid)):
        for box in range(len(rows)):

            if ((soldier["place"][0] == box["x_place"] and soldier["place"][0][0] == box["y_place"]) or
                    (soldier["place"][0] == box["x_place"] and soldier["place"][0][1] == box["y_place"])):
                if box["type"] == "flag":
                    soldier["touched_a_flag"] = True

            if ((soldier["place"][1] == box["x_place"] and soldier["place"][1][0] == box["y_place"]) or
                    (soldier["place"][1] == box["x_place"] and soldier["place"][1][1] == box["y_place"])):
                if box["type"] == "flag":
                    soldier["touched_a_flag"] = True

            if ((soldier["place"][2] == box["x_place"] and soldier["place"][2][0] == box["y_place"]) or
                    (soldier["place"][2] == box["x_place"] and soldier["place"][2][1] == box["y_place"])):
                if box["type"] == "flag":
                    soldier["touched_a_flag"] = True
    return False
