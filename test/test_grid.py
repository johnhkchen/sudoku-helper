import pytest
from sudoku_helper import SudokuGrid


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
def sector_code():
    return [
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
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


def test_grid_get_sector(my_numbers, my_grid, sector_code):
    # Sudoku grid is broken into 9 3x3 sectors
    # We can get all numbers in a sector similar to grid and row
    for sector in range(9):
        answer = [
            [my_numbers[y][x] for y in range(9) if sector_code[y][x] == sector]
            for x in range(9)
        ]
        answer = [row for row in answer if len(row) > 0]
        assert len(answer) == 3
        assert all(len(row) == 3 for row in answer)
        query = my_grid.get_sector(sector)
        assert len(query) == 3
        assert all(len(row) == 3 for row in query)
        for ans_row, query_row in zip(answer, query):
            assert all([ans == elem for ans, elem in zip(ans_row, query_row)])


def test_grid_get_sector_flat(my_grid):
    # Can query sector as a flat list
    # Creates similar behavior as get_row and get_col
    for sector in range(9):
        query = my_grid.get_sector_flat(sector)
        nested_values = my_grid.get_sector(sector)
        flattened = [item for row in nested_values for item in row]
        assert len(query) == 9
        assert all([ans == elem for ans, elem in zip(flattened, query)])


def test_grid_set(my_numbers, my_grid):
    # Syntax: set(x, y, value)
    assert my_grid.get(4, 6) == my_numbers[6][4]
    my_grid.set(4, 6, 8)
    assert my_grid.get(4, 6) == 8
