from sudoku_helper.utils import get_sector_coords


class SudokuGrid:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid

    def get(self, x, y) -> int:
        if x in range(9) and y in range(9):
            return self.grid[y][x]
        else:
            return -1

    def get_row(self, y) -> list[int]:
        return self.grid[y]

    def get_col(self, x) -> list[int]:
        return [self.grid[y][x] for y in range(9)]

    def get_sector(self, sector) -> list[int]:
        return [self.get(x, y) for x, y in get_sector_coords(sector)]

    def set(self, x, y, value):
        if x in range(9) and y in range(9):
            self.grid[y][x] = value
