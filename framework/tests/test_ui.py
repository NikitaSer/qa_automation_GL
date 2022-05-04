def test_login_failed(ui_app):
    """Test user can't login with wrong credentials"""
    ui_app.login_page.login("wrong_email@gmail.com", "wrong_pass")
    ui_app.login_page.assert_login_failed()


def test_sign_up_link(ui_app):
    """Test for check that sign_up link is present on the login page"""
    ui_app.login_page.assert_sign_up_link_is_present()
