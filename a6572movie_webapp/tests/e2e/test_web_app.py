import pytest

from flask import session


def test_login_without_auth(client):
    # Check that we can retrieve the articles page.
    response = client.post('/login')
    assert response.status_code == 404


def test_logout_without_auth(client):
    # Check that we can retrieve the articles page.
    response = client.post('/logout')
    assert response.status_code == 404



def test_home_without_auth(client):
    # Check that we can retrieve the articles page.
    response = client.post('/home/1?keyword=test')
    assert response.status_code == 405