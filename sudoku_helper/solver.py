from collections import defaultdict
from sudoku_helper.utils import get_sector_coords


def unique_candidate(candidates_list: list[list[int]]):
    occurences = defaultdict(lambda: 0)
    for candidates in candidates_list:
        for candidate in candidates:
            occurences[candidate] = occurences[candidate] + 1
    for key in occurences.keys():
        if occurences[key] == 1:
            return key
    return None


def row_candidates(candidates, coords):
    return [candidates[coords[1]][x] for x in range(9)]


def col_candidates(candidates, coords):
    return [candidates[y][coords[0]] for y in range(9)]


def sector_candidates(candidates, coords):
    return [candidates[y][x] for x, y in get_sector_coords(*coords)]


def only_possible_candidate(candidates, coords):
    related_candidates = [
        row_candidates(candidates, coords),
        col_candidates(candidates, coords),
        sector_candidates(candidates, coords),
    ]
    x, y = coords
    for group in related_candidates:
        found_candidate = unique_candidate(group)
        if found_candidate and found_candidate in candidates[y][x]:
            return found_candidate
    return None
