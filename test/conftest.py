import pytest

from fixtures.easy_puzzles import all_easy_puzzles


@pytest.fixture
def easy_puzzles():
    return all_easy_puzzles()
