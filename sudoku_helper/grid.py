from sudoku_helper.utils import sector_code, get_sector_coords, is_valid_coord


class SudokuPuzzle:
    def __init__(self, grid: list[list[int]]) -> None:
        assert len(grid) == 9 and len(grid[0]) == 9
        self.grid = grid
        self.candidates = [[[] for x in range(9)] for y in range(9)]

    def get(self, x, y) -> int:
        return self.grid[y][x] if is_valid_coord(x, y) else -1

    def get_row(self, y) -> list[int]:
        return [self.get(x, y) for x in range(9)]

    def get_col(self, x) -> list[int]:
        return [self.get(x, y) for y in range(9)]

    def get_coords(self, coords) -> list[int]:
        return [self.get(x, y) for x, y in coords]

    def get_sector(self, x, y) -> list[int]:
        return self.get_coords(get_sector_coords(sector_code(x, y)))

    def set(self, x, y, value) -> None:
        if is_valid_coord(x, y):
            self.grid[y][x] = value

    def set_candidates(self, x, y, candidates) -> None:
        self.candidates[y][x] = candidates

    def deduce_candidates(self, x, y) -> list[int]:
        # Deduce candidates for a single cell, returning the list
        if self.get(x, y) != 0:
            return []
        row = self.get_row(y)
        col = self.get_col(x)
        sector = self.get_sector(x, y)
        used_numbers = set(row)
        used_numbers.update(col)
        used_numbers.update(sector)
        return [i for i in range(1, 10) if i not in used_numbers]

    def update_candidates(self) -> None:
        for y in range(9):
            for x in range(9):
                self.set_candidates(
                    x,
                    y,
                    self.deduce_candidates(x, y),
                )

    def get_candidates(self, x, y) -> list[int]:
        return self.candidates[y][x] if is_valid_coord(x, y) else []

    def iterate_solving(self):
        self.update_candidates()
        for y in range(9):
            for x in range(9):
                candidates = self.get_candidates(x, y)
                if len(candidates) == 1:
                    self.set(x, y, candidates[0])
