from sudoku_helper.utils import get_sector_coords, is_valid_coord


class SudokuGrid:
    def __init__(self, grid: list[list[int]]) -> None:
        assert len(grid) == 9 and len(grid[0]) == 9
        self.grid = grid

    def get(self, x, y) -> int:
        return self.grid[y][x] if is_valid_coord(x, y) else -1

    def get_row(self, y) -> list[int]:
        return [self.get(x, y) for x in range(9)]

    def get_col(self, x) -> list[int]:
        return [self.get(x, y) for y in range(9)]

    def get_coords(self, coords) -> list[int]:
        return [self.get(x, y) for x, y in coords]
    
    def get_sector(self, sector) -> list[int]:
        return self.get_coords(get_sector_coords(sector))

    def set(self, x, y, value):
        if is_valid_coord(x, y):
            self.grid[y][x] = value
