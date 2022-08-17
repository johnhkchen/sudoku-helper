import pytest
from sudoku_helper import SudokuPuzzle
from sudoku_helper.utils import get_sector_coords


@pytest.fixture
def easy_numbers():
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
def easy_puzzle(easy_numbers):
    # Initialize a sudoku grid by feeding it a 2D list
    # Sudoku grids are 9x9, with 0's representing blank and 1-9 being numbers
    return SudokuPuzzle(easy_numbers)


def test_grid_get(easy_numbers, easy_puzzle):
    # Grid can be accessed via cartesian coordinate
    # Origin is at top left corner
    # Invalid coordinates return -1
    assert easy_puzzle.get(1, 0) == easy_numbers[0][1]
    assert easy_puzzle.get(2, 2) == easy_numbers[2][2]
    assert easy_puzzle.get(4, 5) == easy_numbers[5][4]
    assert easy_puzzle.get(8, 8) == easy_numbers[8][8]
    assert easy_puzzle.get(-1, -1) == -1
    assert easy_puzzle.get(9, 9) == -1


def test_grid_get_coords(easy_numbers, easy_puzzle):
    # Can also get with a list of coords
    answer = []
    coords = []
    for y in range(9):
        for x in range(9):
            coords.append((x, y))
            answer.append(easy_numbers[y][x])
    query = easy_puzzle.get_coords(coords)
    assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_row(easy_numbers, easy_puzzle):
    for y in range(9):
        answer = [easy_numbers[y][x] for x in range(9)]
        query = easy_puzzle.get_row(y)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_col(easy_numbers, easy_puzzle):
    for x in range(9):
        answer = [easy_numbers[y][x] for y in range(9)]
        query = easy_puzzle.get_col(x)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_sector(easy_numbers, easy_puzzle):
    # Sudoku grid is broken into 9 3x3 sectors
    # get_sector returns the numbers in given sector as a flattened list
    # We can get all numbers in a sector similar to grid and row
    for sector in range(9):
        answer = [easy_numbers[y][x] for x, y in get_sector_coords(sector)]
        query = easy_puzzle.get_sector(sector)
        assert len(query) == len(answer)
        assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_get_sector_using_coords(easy_numbers, easy_puzzle):
    # Sector can also be queried using x, y coords to mimic row/col behavior
    answer = [easy_numbers[y][x] for x, y in get_sector_coords(0)]
    query = easy_puzzle.get_sector_with_coords(0, 0)
    assert len(query) == len(answer)
    assert all([ans == elem for ans, elem in zip(answer, query)])


def test_grid_set(easy_numbers, easy_puzzle):
    # Syntax: set(x, y, value)
    assert easy_puzzle.get(4, 6) == easy_numbers[6][4]
    easy_puzzle.set(4, 6, 8)
    assert easy_puzzle.get(4, 6) == 8


def test_candidates_matrix_exists(easy_puzzle):
    assert easy_puzzle.candidates is not None
    assert len(easy_puzzle.candidates) == 9
    for y in range(9):
        assert len(easy_puzzle.candidates[y]) == 9
        for x in range(9):
            assert len(easy_puzzle.candidates[y][x]) == 0


def test_deduce_candidates(easy_puzzle):
    # The only candidate is 1 for (0, 1) in the easy puzzle
    candidates = easy_puzzle.deduce_candidates(0, 1)
    assert len(candidates) == 1 and candidates[0] == 1


def test_deduce_candidates_solved(easy_puzzle):
    # A filled in slot has no candidates
    candidates = easy_puzzle.deduce_candidates(1, 0)
    assert len(candidates) == 0


def test_update_candidates(easy_puzzle):
    easy_puzzle.update_candidates()
    # The only candidate is 7 for (0, 0) in the easy puzzle
    candidates = easy_puzzle.get_candidates(0, 0)
    assert len(candidates) == 1 and candidates[0] == 7
    # The only candidate is 1 for (0, 1) in the easy puzzle
    candidates = easy_puzzle.get_candidates(0, 1)
    assert len(candidates) == 1 and candidates[0] == 1


def test_iterate_solving(easy_puzzle):
    # Single-candidates solvable on first iteration:
    # (0, 0) -> 7
    # (0, 1) -> 1
    # (0, 2) -> 4
    coords = [(0, 0), (0, 1), (0, 2)]
    answer = [0, 0, 0]
    query = easy_puzzle.get_coords(coords)
    assert all([ans == elem for ans, elem in zip(answer, query)])

    easy_puzzle.iterate_solving()
    answer = [7, 1, 4]
    query = easy_puzzle.get_coords(coords)
    assert all([ans == elem for ans, elem in zip(answer, query)])
