import pytest

from flask import session


def test_movies_with_pagenum(client):
    # Check that we can retrieve the articles page.
    response = client.get('/home/1')
    assert response.status_code == 200
    # Check that all articles on the requested date are included on the page.
    assert b'Avengers' in response.data


def test_movies_with_error_pagenum(client):
    # Check that we can retrieve the articles page.
    response = client.get('/home/10')
    assert response.status_code == 200
    # Check that all articles on the requested date are included on the page.
    assert b'Avengers' not in response.data


def test_movies_without_pagenum(client):

    response = client.get('/home')
    assert response.status_code == 404


def test_movies_post_pagenum(client):
    response = client.post(
        '/home/1',
        data={'username': 't'}
    )
    assert response.status_code == 405