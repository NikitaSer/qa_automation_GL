import pytest
from app.api.client import ApiClient


@pytest.fixture(scope="session")
def api_session():
    """Fixture for initializing ApiClient object and performs user's authentication"""
    api_client = ApiClient()
    api_client.login()
    yield api_client
