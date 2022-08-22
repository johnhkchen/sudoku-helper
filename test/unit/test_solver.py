import pytest
import random

from sudoku_helper import solver
from sudoku_helper.utils import get_sector_coords


def test_solver_exists():
    assert solver


def test_input_for_unique_candidate():
    # To solve harder problems, we find unique candidates
    row_candidates = [[2, 3, 4] for _ in range(9)]
    col_candidates = [[2, 3, 8] for _ in range(9)]
    sector_candidates = [[3, 4, 8] for _ in range(8)]
    sector_candidates.append([3, 4, 8, 9])

    assert 9 in sector_candidates[8]
    assert 9 not in row_candidates[8]
    assert 9 not in col_candidates[8]
    for i in range(8):
        assert 9 not in sector_candidates[i]
        assert 9 not in row_candidates[i]
        assert 9 not in col_candidates[i]


def test_solver_unique_candidates_callable():
    # Use the test input created previously and pass it to the solver
    row_candidates = [[2, 3, 4] for _ in range(9)]
    col_candidates = [[2, 3, 8] for _ in range(9)]
    sector_candidates = [[3, 4, 8] for _ in range(8)]
    sector_candidates.append([3, 4, 8, 9])
    # The only unique candidate is 9 and should be found by unique_candidate
    # when it is given the sector candidates list
    assert solver.unique_candidate(row_candidates) is None
    assert solver.unique_candidate(col_candidates) is None
    assert solver.unique_candidate(sector_candidates) == 9


@pytest.fixture
def simple_candidates():
    return [[[i] for _ in range(9)] for i in range(9)]


@pytest.fixture
def sample_candidates():
    # Calculate using a hard problem, using this module
    return [
        [[2, 3, 4], [], [], [], [2, 3, 8], [3, 4], [], [2, 3, 4, 8], [2, 3, 4, 8, 9]],
        [[2, 3, 4], [], [], [1, 3, 4, 8], [], [1, 3, 4], [2, 4, 8], [], [2, 3, 4, 8]],
        [[], [2, 3, 4], [], [], [2, 3], [3, 4, 5], [], [2, 3, 4], [2, 3, 4, 6]],
        [
            [3, 4, 7],
            [3, 4, 7],
            [],
            [1, 3, 4, 7],
            [1, 3, 9],
            [],
            [2, 4, 9],
            [],
            [1, 2, 4, 7, 9],
        ],
        [
            [3, 4, 7, 8],
            [3, 4, 7, 8],
            [],
            [1, 3, 4, 7],
            [],
            [1, 3, 4, 7, 9],
            [],
            [4, 7, 8],
            [1, 4, 7, 8, 9],
        ],
        [[4, 6, 7, 8], [], [], [], [], [4, 7], [], [4, 7, 8], [4, 7, 8]],
        [[7, 8, 9], [7, 8], [], [1, 7, 8], [1, 8, 9], [], [4, 6, 8], [4, 7, 8], []],
        [[2, 5, 7, 8], [], [], [3, 5, 7, 8], [], [3, 5, 7], [2, 8], [], [2, 3, 7, 8]],
        [
            [2, 5, 7, 8, 9],
            [2, 7, 8],
            [],
            [3, 5, 7, 8],
            [3, 8, 9],
            [],
            [2, 8],
            [],
            [2, 3, 7, 8],
        ],
    ]


def test_simple_candidates(simple_candidates):
    assert simple_candidates[1] == [[1], [1], [1], [1], [1], [1], [1], [1], [1]]

    assert simple_candidates[8] == [[8], [8], [8], [8], [8], [8], [8], [8], [8]]


def test_solver_row_candidates(simple_candidates):
    # It should return a row of candidates from a grid
    coord = (1, 8)
    expected_answer = [[8], [8], [8], [8], [8], [8], [8], [8], [8]]
    ans = solver.row_candidates(simple_candidates, coord)
    assert ans == expected_answer


def test_solver_col_candidates(simple_candidates):
    # It should return a column of candidates from a grid
    coord = (1, 8)
    expected_answer = [[0], [1], [2], [3], [4], [5], [6], [7], [8]]
    ans = solver.col_candidates(simple_candidates, coord)
    assert ans == expected_answer


def test_solver_sector_candidates(simple_candidates):
    # It should return a sector's candidates from a grid
    coord = (1, 8)
    # Bottom left sector
    expected_answer = [[6], [6], [6], [7], [7], [7], [8], [8], [8]]
    ans = solver.sector_candidates(simple_candidates, coord)

    assert ans == expected_answer


def test_solver_row_candidates_harder(sample_candidates):
    # It should return a row of candidates from a grid
    coord = (random.randint(0, 8), random.randint(0, 8))
    expected_answer = [sample_candidates[coord[1]][x] for x in range(9)]
    ans = solver.row_candidates(sample_candidates, coord)
    assert ans == expected_answer


def test_solver_col_candidates_harder(sample_candidates):
    # It should return a column of candidates from a grid
    coord = (random.randint(0, 8), random.randint(0, 8))
    expected_answer = [sample_candidates[y][coord[0]] for y in range(9)]
    ans = solver.col_candidates(sample_candidates, coord)
    assert ans == expected_answer


def test_solver_sector_candidates_harder(sample_candidates):
    # It should return a sector's candidates from a grid
    coord = (random.randint(0, 8), random.randint(0, 8))
    expected_answer = [sample_candidates[y][x] for x, y in get_sector_coords(*coord)]
    ans = solver.sector_candidates(sample_candidates, coord)
    assert ans == expected_answer


def test_solver_finds_only_possible_candidate_real_1(sample_candidates):
    # The way we call the function is messy so we'll call a helper function
    # Pass it the grid and a coord, and it will handle the rest

    # In the top-right sector, 9 appears only once as a candidate
    target = (8, 0)
    solution = 9
    assert solution == solver.only_possible_candidate(sample_candidates, target)


def test_solver_finds_only_possible_candidate_real_2(sample_candidates):
    # In the top-right sector, 5 appears only once as a candidate
    target = (5, 2)
    solution = 5
    assert solution == solver.only_possible_candidate(sample_candidates, target)
