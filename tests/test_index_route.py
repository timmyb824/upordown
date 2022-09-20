import pytest

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Simple Up or Down Tool</h1>" in response.data

