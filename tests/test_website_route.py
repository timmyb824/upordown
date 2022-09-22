import pytest

def test_website_route_http_method_bad(client):
    response = client.get('/website')
    assert response.status_code == 405

def test_website_route_http_method_good(client):
    response = client.post('/website', data={'website': 'https://google.com'})
    assert response.status_code == 200

