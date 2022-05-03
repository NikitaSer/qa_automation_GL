import pytest


@pytest.fixture
def ui_app():
    yield CosmosIDUI()


def test_login_failed(ui_app):
    """Test user cannot login with wrong creds"""
    assert ui_app.login('kjshdfkjh@kkf.com', 'asdfasdf')
    .assert_login_failed() is False


def test_username_field_exists(ui_app):
    """Test user cannot login with wrong creds"""
    assert ui_app.login_page.assert_username_exists()
