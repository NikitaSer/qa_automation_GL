import pytest
from app.api.client import ApiClient
from app.ui.cosmos_id_ui import CosmosIDUI


@pytest.fixture(scope="session")
def api_session():
    """Fixture for initializing ApiClient object and performs user's authentication"""
    api_client = ApiClient()
    api_client.login()
    yield api_client


@pytest.fixture(scope="session")
def ui_app(request):
    """Fixture for initializing web app instance CosmosIDUI()"""
    browser = request.config.getoption("browser")
    app = CosmosIDUI(browser=browser)
    app.launch_browser()
    yield app
    app.close_browser()
