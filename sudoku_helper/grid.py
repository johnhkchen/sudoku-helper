class SudokuGrid:
    sector_code = (
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
    )

    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid

    def get(self, x, y) -> int:
        # Returns -1 if out of range
        if x in range(9) and y in range(9):
            return self.grid[y][x]
        else:
            return -1

    def get_row(self, y) -> list[int]:
        return self.grid[y]

    def get_col(self, x) -> list[int]:
        return [self.grid[y][x] for y in range(9)]

    def get_sector(self, sector) -> list[list[int]]:
        raw_query = []
        for y in range(9):
            values_in_sector = [
                self.get(x, y) for x in range(9) if self.sector_code[y][x] == sector
            ]
            for row in values_in_sector:
                if len(row) == 3:
                    raw_query.append(row)
        return raw_query

    def get_sector_flat(self, sector) -> list[int]:
        return [n for row in self.get_sector(sector) for n in row]

    def set(self, x, y, value):
        if x in range(9) and y in range(9):
            self.grid[y][x] = value
