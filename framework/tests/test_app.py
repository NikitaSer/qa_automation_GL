from app.api.client import ApiClient

api_client = ApiClient()


def test_login_successful():
    api_client.login()
    assert api_client.token is not None

def test_root_folders():
    api_client.get_folders()
