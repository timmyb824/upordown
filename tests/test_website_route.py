import pytest

def test_website_route_bad_http_method(client):
    response = client.get('/website')
    assert response.status_code == 405

def test_website_route_good_http_method(client):
    response = client.post('/website', data={'website': 'https://google.com'})
    assert response.status_code == 200