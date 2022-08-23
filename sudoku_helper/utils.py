# Helper functions for things that get reused between modules
import random


def sector_code(x: int, y: int) -> int:
    if is_valid_coord(x, y):
        return (
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
        )[y][x]
    else:
        return -1


def is_valid_coord(x: int, y: int) -> bool:
    return x in range(9) and y in range(9)


def get_sector_coords(x_given: int, y_given: int) -> list[tuple[int, int]]:
    # return a list of 9 (x, y) coordinates for a given sector
    sector = sector_code(x_given, y_given)
    coords = []
    for y in range(9):
        for x in range(9):
            if sector_code(x, y) == sector:
                coords.append((x, y))
    return coords


def has_thick_vertical_divider(x):
    return x % 3 == 0


def has_thick_horizontal_divider(y):
    return y % 3 == 0


def get_row_substring(x, left, middle, divider_thin, divider_thick, right, n=7):
    # Return the corresponding segment above a cell
    spacer = middle * n
    if x == 0:
        return left + spacer
    elif x == 8:
        return divider_thin + spacer + right
    else:
        if has_thick_vertical_divider(x):
            return divider_thick + spacer
        else:
            return divider_thin + spacer


def get_table_border(x, y):
    if y == 0:
        return get_row_substring(x, "┏", "━", "┯", "┳", "┓")
    elif y == 9:
        return get_row_substring(x, "┗", "━", "┷", "┻", "┛")
    else:
        if has_thick_horizontal_divider(y):
            return get_row_substring(x, "┣", "━", "┿", "╋", "┫")
        else:
            return get_row_substring(x, "┠", "─", "┼", "╂", "┨")


def print_box_border(y):
    for x in range(9):
        print(get_table_border(x, y), end="")


def get_cell_characters(x, y):
    if has_thick_vertical_divider(x):
        return "┃"
    else:
        return "│"


def print_cell_row(y):
    for x in range(9):
        print(get_cell_characters(x, y), end="")
        print(str().center(7), end="")
    print("┃")
    for x in range(9):
        cell_value = random.randint(1, 9)
        print(get_cell_characters(x, y), end="")
        print(str(cell_value).center(7), end="")
    print("┃")
    for x in range(9):
        print(get_cell_characters(x, y), end="")
        print(str().center(7), end="")
    print("┃")


def print_box():
    for y in range(9):
        print_box_border(y)
        print()
        print_cell_row(y)
    print_box_border(9)
    print()


def print_sudoku(puzzle):
    # Prints a 2D list of numbers as a formatted sudoku grid
    is_thick = False
    for row in puzzle:
        print(" ", end="")
        for elem in row:
            if type(elem) != int:
                if len(elem) == 1:
                    elem = "{}!".format(elem[0])
                else:
                    elem = ",".join([str(c) for c in elem])
            else:
                elem = " " if elem == 0 else elem
            vertical_divider = "┃" if is_thick else "|"
            print("{}".format(str(elem).center(9)), end=vertical_divider)
        print("\n┣", end="")
        for i in range(9):
            print("━" * 10, end="")
        print("")
    print("\n")
