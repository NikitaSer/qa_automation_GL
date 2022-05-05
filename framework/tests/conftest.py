import pytest
from selenium import webdriver
from app.api.client import ApiClient
from app.ui.cosmos_id_ui import CosmosIDUI


@pytest.fixture(scope="session")
def api_session():
    """Fixture for initializing ApiClient object and performs user's authentication"""
    api_client = ApiClient()
    api_client.login()
    yield api_client


@pytest.fixture(scope="session")
def ui_app():
    """Fixture for initializing web app instance CosmosIDUI()"""
    app = CosmosIDUI(browser)
    app.launch_browser()
    yield app
    app.quit()
