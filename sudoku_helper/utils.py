# Helper functions for things that get reused between modules
sector_code = (
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
)


def is_valid_coord(x, y):
    return x in range(9) and y in range(9)


def get_sector_coords(sector):
    # return a list of 9 (x, y) coordinates for a given sector
    coords = []
    for y in range(9):
        for x in range(9):
            if sector_code[y][x] == sector:
                coords.append((x, y))
    return coords
