from app.ui.page_objects.login_page import LoginPage


class CosmosIDUI:
    """Class defining web app"""

    def __init__(self, browser):
        sefl.driver = BrowsersProvider.get_browser(browser)
        self.login_page = LoginPage(driver)
