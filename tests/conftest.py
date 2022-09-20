import pytest
from src.main import app

@pytest.fixture
def client():
    return app.test_client()