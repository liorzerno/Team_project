import consts
import random

#box = {x_place: x, y_place: y, type: "mine"/ "flag" / "empty"}
#field_grid = [box, box...]

flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS
field_grid = []
mines_list = []

def field_initialization():
    """
    Initializes the field grid.
    :return: grid of rows and columns containing a box dictionary.
    """
    global field_grid
    new = []

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            new.append(create_box(row, col))
        field_grid.append(new)
        print(new)
        new = []

    return field_grid

def create_box(row, col):
    global field_grid
    global mines_list
    tup = (row, col)
    is_mine = False

    for mine in mines_list:
        mine_cols = mine[1]

        if tup[0] == mine[0] and tup[1] in mines_list:
            is_mine = True

    if is_mine:
        box = {"x_place": row, "y_place": col, "type": "mine"}
    else:
        box = {"x_place": row, "y_place": col, "type": "empty"}

    return box


def mine_randomizer():
    """
    Makes a list of mine's index.
    :return: a list of indexes that contain a mine.
    """
    global mines_list

    for i in range(consts.MINES_COUNT):
        is_existing = False

        while not is_existing:
            rnd_row = random.randint(0, consts.BOARD_ROWS - 1)
            rnd_col = random.randint(0, consts.BOARD_COLS - 3)
            tup = (rnd_row, [rnd_col, rnd_col + 1, rnd_col + 2])

            if tup not in mines_list:
                mines_list.append(tup)
                is_existing = True


def is_flag():
    pass

def is_mine():
    pass

field_grid = field_initialization()
