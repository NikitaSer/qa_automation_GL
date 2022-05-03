
class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def prepare_url(self, url):
        return Config.BASE_URL + url

    def enter_text(self, text, element):
        # waiter 
        element = self.driver.find_element(**element)
        element.send_keys(text)

    def click(self, element):
        element = self.driver.find_element(**element)
        element.click()

    def inproper_click():
        pass
