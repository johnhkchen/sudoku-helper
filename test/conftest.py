import pytest

from fixtures.easy_puzzles import all_easy_puzzles
from fixtures.medium_puzzles import all_medium_puzzles
from fixtures.hard_puzzles import all_hard_puzzles


@pytest.fixture
def easy_puzzles():
    return all_easy_puzzles()


@pytest.fixture
def medium_puzzles():
    return all_medium_puzzles()


@pytest.fixture
def hard_puzzles():
    return all_hard_puzzles()
