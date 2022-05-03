from framework.app.ui.page_objects.login_page import LoginPage


class CosmosIDUI:

    def __init__(self) -> None:
        self.login_page = LoginPage()

    def login(self):
        self.login_page.login()

    def switch_menu_item(self, new_possition):
        pass

    def create_user(self, new_username):
        pass
