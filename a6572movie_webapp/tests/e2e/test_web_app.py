import pytest

from flask import session


def test_movies_with_pagenum(client):
    # Check that we can retrieve the articles page.
    response = client.post('/login')
    assert response.status_code == 404



