from sudoku_helper import SudokuPuzzle


def test_medium_puzzles_filled(medium_puzzles):
    # Puzzles should all be filled in
    for puzzle in medium_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(18):
            sudoku.iterate_solving()
        for row in sudoku.grid:
            assert 0 not in row


def test_medium_puzzles_solved(medium_puzzles):
    # Puzzles should be solved correctly
    for puzzle in medium_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(18):
            sudoku.iterate_solving()
        assert sudoku.grid == puzzle["solved"]
