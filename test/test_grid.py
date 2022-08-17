import pytest
from sudoku_helper import SudokuGrid
from sudoku_helper.utils import get_sector_coords


@pytest.fixture
def my_numbers():
    # Current test numbers
    # Subject to change, but a source of truth
    # This one is a valid sudoku puzzle of easy difficulty
    return [
        [0, 9, 3, 8, 4, 6, 0, 1, 0],
        [0, 2, 0, 9, 3, 0, 0, 7, 4],
        [0, 5, 8, 1, 7, 0, 3, 9, 0],
        [0, 0, 0, 0, 0, 4, 7, 0, 1],
        [2, 0, 7, 0, 0, 1, 5, 0, 0],
        [6, 0, 5, 0, 0, 8, 0, 0, 0],
        [8, 0, 0, 2, 6, 0, 0, 0, 9],
        [0, 0, 0, 0, 1, 0, 0, 8, 0],
        [9, 0, 1, 0, 0, 0, 0, 3, 2],
    ]


@pytest.fixture
def my_grid(my_numbers):
    # Initialize a sudoku grid by feeding it a 2D list
    # Sudoku grids are 9x9, with 0's representing blank and 1-9 being numbers
    return SudokuGrid(my_numbers)


def test_grid_get(my_numbers, my_grid):
    # Grid can be accessed via cartesian coordinate
    # Origin is at top left corner
    # Invalid coordinates return -1
    assert my_grid.get(1, 0) == my_numbers[0][1]
    assert my_grid.get(2, 2) == my_numbers[2][2]
    assert my_grid.get(4, 5) == my_numbers[5][4]
    assert my_grid.get(8, 8) == my_numbers[8][8]
    assert my_grid.get(-1, -1) == -1
    assert my_grid.get(9, 9) == -1


def test_grid_get_coords(my_numbers, my_grid):
    # Can also get with a list of coords
    answer = []
    coords = []
    for y in range(9):
        for x in range(9):
            coords.append((x, y))
            answer.append(my_numbers[y][x])
    query = my_grid.get_coords(coords)
    assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_row(my_numbers, my_grid):
    for y in range(9):
        answer = [my_numbers[y][x] for x in range(9)]
        query = my_grid.get_row(y)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_col(my_numbers, my_grid):
    for x in range(9):
        answer = [my_numbers[y][x] for y in range(9)]
        query = my_grid.get_col(x)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_sector(my_numbers, my_grid):
    # Sudoku grid is broken into 9 3x3 sectors
    # get_sector returns the numbers in given sector as a flattened list
    # We can get all numbers in a sector similar to grid and row
    for sector in range(9):
        answer = [my_numbers[y][x] for x, y in get_sector_coords(sector)]
        query = my_grid.get_sector(sector)
        assert len(query) == len(answer)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_set(my_numbers, my_grid):
    # Syntax: set(x, y, value)
    assert my_grid.get(4, 6) == my_numbers[6][4]
    my_grid.set(4, 6, 8)
    assert my_grid.get(4, 6) == 8
