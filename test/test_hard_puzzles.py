import pytest

from sudoku_helper import SudokuPuzzle


@pytest.mark.xfail
def test_hard_puzzles_filled(hard_puzzles):
    # Puzzles should all be filled in
    for puzzle in hard_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(18):
            sudoku.iterate_solving()
        for row in sudoku.grid:
            assert 0 not in row


@pytest.mark.xfail
def test_hard_puzzles_solved(hard_puzzles):
    # Puzzles should be solved correctly
    for puzzle in hard_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(18):
            sudoku.iterate_solving()
        assert sudoku.grid == puzzle["solved"]
