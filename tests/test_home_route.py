import pytest
from src.main import get_status_code, url_status_code, multi_url_status_code

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Simple Up or Down Tool</h1>" in response.data

def test_homepage_bad_http_method(client):
    response = client.post('/')
    assert response.status_code == 405

def test_get_status_code_good():
    status_code = get_status_code('https://www.google.com')
    assert status_code == 200

def test_get_status_code_bad():
    status_code = get_status_code('https://wwww.google.com')
    assert status_code == 'UNREACHABLE'

def test_url_status_code_good():
    status_code = url_status_code('https://www.google.com')
    assert status_code == '200'

def test_url_status_code_bad():
    status_code = url_status_code('https://wwww.google.com')
    assert status_code == 'UNREACHABLE'

def test_multiple_url_status_code():
    status_items = list(multi_url_status_code())
    assert status_items == [('https://duplicati.local.timmybtech.com', '302'), ('https://gitea.local.timmybtech.com', '200'), ('https://doesnotexist.bbc.co.uk', 'UNREACHABLE'), ('https://grafana.local.timmybtech.com', '302'), ('https://speedtest.local.timmybtech.com', '200'), ('https://code-server.local.timmybtech.com', '302')]
