import pytest

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Simple Up or Down Tool</h1>" in response.data

def test_homepage_bad_http_method(client):
    response = client.post('/')
    assert response.status_code == 405

def test_website_route_http_method_bad(client):
    response = client.get('/website')
    assert response.status_code == 405

def test_website_route_http_method_good(client):
    response = client.post('/website', data={'website': 'https://google.com'})
    assert response.status_code == 200