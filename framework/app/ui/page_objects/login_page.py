class LoginPage(BasePage):
    USERNAME_FIELD = {'type': By.Xpath, 'valus': '//*[@id="email"]'}
    PASS_FIELD = (By.Xpath, '//*[@id="password"]')
    LOGIN_BTN = (By.Xpath, '//*[@id="signInButton"]')
    LOGIN_ERR = "/div/div"

    def __init__(self, driver) -> None:
        super(driver)

    def login(self, username, password):
        url = self.prepare_url(Url.LOGIN)
        self.driver.get(url)

        self.enter_text(username, LoginPage.USERNAME_FIELD)
        self.enter_text(password, LoginPage.USERNAME_FIELD)

        self.click(By.path, LoginPage.LOGIN_BTN)

        return True

    def go_to_register_page(self):
        pass

    def assert_login_failed(self):
        element = self.get_element(LOGIN_ERR)
        if element is not None:
            return True

    def assert_username_exists(self):
        element = self.get_element(LoginPage.USERNAME_FIELD)
        if element is not None:
            return True
