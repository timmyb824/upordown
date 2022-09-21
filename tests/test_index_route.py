import pytest

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Simple Up or Down Tool</h1>" in response.data

def test_website_route_bad_http_method(client):
    response = client.post('/website')
    assert response.status_code == 400

def test_index_route_good_http_method(client):
    response = client.get('/', data={'website': 'https://gitea.local.timmybtech.com'})
    assert response.status_code == 200
