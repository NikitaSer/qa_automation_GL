from framework.app.ui.page_objects.login_page import LoginPage
from framework.providers.browsers import Browsers
from framework.config.config import Config


class CosmosIDUI:
    """Class defining web app"""

    def __init__(self, browser):
        self.driver = Browsers.get_browser(browser).init_driver()
        self.login_page = LoginPage(self.driver)

    def launch_browser(self):
        """Method for opening browser on the BASE_URL"""
        self.driver.get(url=Config.BASE_URL)

    def close_browser(self):
        """Method for closing browser"""
        self.driver.quit()
