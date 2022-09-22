import pytest
from src.main import get_status_code

def test_homepage_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Simple Up or Down Tool</h1>" in response.data

def test_homepage_route_bad_http_method(client):
    response = client.post('/')
    assert response.status_code == 405

# def test_index_route_good_http_method(client):
#     response = client.get('/', data={'website': 'https://gitea.local.timmybtech.com'})
#     assert response.status_code == 200

def test_get_status_code_good():
    status_code = get_status_code('https://www.google.com')
    assert status_code == 200

def test_get_status_code_bad():
    status_code = get_status_code('https://wwww.google.com')
    assert status_code == 'UNREACHABLE'


