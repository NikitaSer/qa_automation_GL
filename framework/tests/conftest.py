import pytest
from app.api.client import ApiClient


@pytest.fixture(scope='session')
def api_client():
    """Fixture for initializing ApiClient object and user's login"""
    api_client = ApiClient()
    api_client.login()
    return api_client
