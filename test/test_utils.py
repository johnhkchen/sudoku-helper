from sudoku_helper.utils import get_sector_coords


def test_get_sector_code():
    for y in range(9):
        for x in range(9):
            coords = get_sector_coords(x, y)
            assert len(coords) == 9
            for x, y in coords:
                assert x in range(9) and y in range(9)
