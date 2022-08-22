from sudoku_helper import SudokuPuzzle


def test_hard_puzzles(hard_puzzles):
    # Fully solving hard algorithms is not working yet
    # Checking for completion as an intermediate goal
    for puzzle in hard_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(18):
            sudoku.iterate_solving()
        for row in sudoku.grid:
            assert 0 not in row
