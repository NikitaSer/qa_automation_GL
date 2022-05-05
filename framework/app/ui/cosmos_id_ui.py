from lib2to3.pgen2 import driver
from app.ui.page_objects.login_page import LoginPage


class CosmosIDUI:
    """Class defining web app"""

    def __init__(self, browser):
        self.driver = BrowsersProvider.get_browser(browser)
        self.login_page = LoginPage(driver)

    def launch_browser(self):
        self.driver.get("")

    def quit(self):
        sefl.driver.terminate()