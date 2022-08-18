from sudoku_helper import SudokuPuzzle


def test_easy_puzzles(easy_puzzles):
    for puzzle in easy_puzzles:
        sudoku = SudokuPuzzle(puzzle["start"])
        for _ in range(6):
            sudoku.iterate_solving()
        assert sudoku.grid == puzzle["solved"]
