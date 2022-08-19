# Helper functions for things that get reused between modules
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


def print_sudoku(puzzle):
    # Prints a 2D list of numbers as a formatted sudoku grid
    print("\n" + "-" * 73)
    for row in puzzle:
        print("|", end="")
        for elem in row:
            if type(elem) != int:
                if len(elem) == 1:
                    elem = "{}!".format(elem[0])
                else:
                    elem = ",".join([str(c) for c in elem])
            else:
                elem = " " if elem == 0 else elem
            print("{}".format(str(elem).center(7)), end="|")
        print("\n" + "-" * 73)
    print("\n")
