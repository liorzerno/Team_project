import consts
import screen
import pygame
x = 0
y = 0
state = {
        "soldier": screen.soldier_display( x, y),
        "is_window_open": True,
        "state": consts.RUNNING_STATE,
        "soldier_moving": False
    }
def put_mines_in_place(field_grid):
    #findes the start of the mine
    # returns a list of where the image needs to be inserted
    insert_image=[]
    for rows in range (consts.BOARD_ROWS - 1):
        for col in range (consts.BOARD_COLS - 3):
            if field_grid[rows][col]["type"] == "mine" and field_grid[rows][col+1]["type"] == "mine" and field_grid[rows][col+2]["type"] == "mine":
                insert_image.append([rows,col])
    return insert_image


# def main():
#     pygame.init()
#     while state["is_window_open"]:
#         screen.draw_game(state)
#
# if __name__ == '__main__':
#     main()

