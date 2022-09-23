import pytest
from src.upordown.main import app
# import src

@pytest.fixture
def client():
    return app.test_client()