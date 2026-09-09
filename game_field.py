import consts
import random

#box = {x_place: x, y_place: y, type: "mine"/ "flag" / "empty"}
#field_grid = [box, box...]

flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS
field_grid = []


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
        new = []

    put_mine_on_field()
    add_flag()
    return field_grid

def create_box(row, col):
    """
    Creates a box given a row and column.
    :param row: a row index.
    :param col: a col index.
    :return: a box dictionary.
    """
    box = {"x_place": row, "y_place": col, "type": "empty"}
    return box


def mine_randomizer():
    """
    Makes a list of mine's index.
    :return: a list of indexes that contain a mine.
    """
    mines_list = []

    for i in range(consts.MINES_COUNT):
        is_existing = False

        while not is_existing:
            rnd_row = random.randint(0, consts.BOARD_ROWS - 1)
            rnd_col = random.randint(0, consts.BOARD_COLS - 3)

            col_list = [rnd_col, rnd_col + 1, rnd_col + 2]
            tup = (rnd_row, col_list)

            if not mine_index_checker(mines_list, rnd_row, rnd_col):
                mines_list.append(tup)
                is_existing = True
    return mines_list

def mine_index_checker(mines_list, row, col):
    """
    Checks if there is already a mine at the given row and col.
    :param mines_list: a list of mine's index.
    :param row: a row index.
    :param col: a col index.
    :return: boolean.
    """
    for mine in mines_list:
        mine_row = mine[0]
        if mine_row == row:
            mine_cols = mine[1]
            if col in mine_cols or col + 1 in mine_cols or col + 2 in mine_cols:
                return True
    return False

def put_mine_on_field():
    """
    Puts a mine type according to the mine list.
    :return: None
    """
    global field_grid
    mine_list = mine_randomizer()

    for mine in mine_list:
        row = mine[0]
        col1 = mine[1][0]
        col2 = mine[1][1]
        col3 = mine[1][2]

        field_grid[row][col1] = {"x_place": row, "y_place": col1, "type": "mine"}
        field_grid[row][col2] = {"x_place": row, "y_place": col2, "type": "mine"}
        field_grid[row][col3] = {"x_place": row, "y_place": col3, "type": "mine"}


def add_flag():
    """
    Adds a flag on the board.
    :return: None
    """
    global field_grid
    rows = consts.BOARD_ROWS
    cols = consts.BOARD_COLS

    for i in range(rows-consts.FLAG_ROWS, rows):
        for j in range(cols-consts.FLAG_COLS, cols):
            field_grid[i][j]["type"] = "flag"


# def put_mines_in_place():
#     #finds the start of the mine
#     # returns a list of where the image needs to be inserted
#     global  field_grid
#     insert_image=[]
#
#     for rows in range (consts.BOARD_ROWS - 1):
#         for col in range (consts.BOARD_COLS - 3):
#             if field_grid[rows][col]["type"] == "mine" and field_grid[rows][col+1]["type"] == "mine" and field_grid[rows][col+2]["type"] == "mine":
#                 insert_image.append([rows,col])
#     return insert_image