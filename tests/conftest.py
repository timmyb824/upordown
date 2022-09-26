import pytest
from src.upordown.main import app
# import src

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def checkurls():
    checkurls = ["https://www.google.com","https://www.msn.com","https://doesnotexist.co.uk","https://www.yahoo.com"]
    return checkurls