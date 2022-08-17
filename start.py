# This script is used to run the program
# python3 start.py
from sudoku_helper import SudokuPuzzle
from sudoku_helper.utils import print_sudoku

def start():    
    my_puzzle = SudokuPuzzle([
        [0, 9, 3, 8, 4, 6, 0, 1, 0],
        [0, 2, 0, 9, 3, 0, 0, 7, 4],
        [0, 5, 8, 1, 7, 0, 3, 9, 0],
        [0, 0, 0, 0, 0, 4, 7, 0, 1],
        [2, 0, 7, 0, 0, 1, 5, 0, 0],
        [6, 0, 5, 0, 0, 8, 0, 0, 0],
        [8, 0, 0, 2, 6, 0, 0, 0, 9],
        [0, 3, 0, 0, 1, 0, 0, 8, 0],
        [9, 0, 1, 0, 0, 0, 0, 3, 2],
    ])
    
    print("Your Sudoku Puzzle: ")
    print_sudoku(my_puzzle.grid)
    for i in range(1, 6):
        my_puzzle.iterate_solving()
        # print("Solving... Iteration {}".format(i))
        # print_sudoku(my_puzzle.grid)
    print("Solved: ")
    print_sudoku(my_puzzle.grid)

if __name__ == "__main__":
    start()
