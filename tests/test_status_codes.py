import pytest
from src.upordown.status_codes import get_status_code, url_status_code, multi_url_status_code

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
    assert status_items == [('https://www.google.com', '200'), ('https://www.msn.com', '200'), ('https://doesnotexist.bbc.co.uk', 'UNREACHABLE'), ('https://www.yahoo.com', '200')]