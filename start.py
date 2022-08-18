# This script is used to run the program
# python3 start.py
from sudoku_helper import SudokuPuzzle
from sudoku_helper.utils import print_sudoku

def start():    
    # Solve the given sudoku puzzle
    my_puzzle = SudokuPuzzle([
        [0, 2, 0, 5, 0, 1, 6, 8, 9],
        [6, 8, 0, 0, 0, 4, 7, 0, 2],
        [1, 9, 7, 0, 8, 0, 0, 0, 0],
        [0, 1, 6, 7, 9, 0, 0, 3, 0],
        [0, 7, 0, 8, 0, 0, 5, 6, 0],
        [8, 0, 0, 0, 1, 2, 0, 0, 0],
        [5, 0, 0, 0, 2, 0, 0, 9, 6],
        [0, 0, 9, 0, 0, 8, 4, 0, 0],
        [2, 0, 1, 3, 0, 0, 0, 0, 7],
    ])
    
    print("Your Sudoku Puzzle: ")
    print_sudoku(my_puzzle.grid)
    for i in range(1, 6):
        my_puzzle.iterate_solving()
        # print("Solving... Iteration {}".format(i))
        # print_sudoku(my_puzzle.grid)
    print("Solved: ")
    print_sudoku(my_puzzle.grid)
    # Print the grid to use as a test case
    # print(my_puzzle.grid)

if __name__ == "__main__":
    start()


# Empty grid for new puzzles:
    # my_puzzle = SudokuPuzzle([
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ])