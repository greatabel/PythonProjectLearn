from datetime import date

from movie.domain.model import Movie

import pytest





# @pytest.fixture()
# def user():
#     return User('dbowie', '1234567890')


@pytest.fixture()
def movie():
    return Movie('matrix', 1998, 1)


def test_movie(movie):
    assert movie.title == 'matrix'
    assert movie.release_year == 1998
    assert movie.id == 1
