import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from framework.config.config import Config
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Class defining common properties and behaviour for the web app pages"""

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, text, element):
        """Reimplementation of find and enter text into text element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        element.send_keys(text)

    def click(self, element):
        """Reimplementation of find element and click on it"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        element.click()

    def get_element(self, element):
        """Reimplementation of find element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        return element

    def is_element_present(self, element, timeout=Config.TIMEOUT):
        """Method-waiter, checking that element is present on the page"""
        try:
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(element)
            )
        except TimeoutException:
            logging.error(f"Cant find element={element} for the timeout={timeout}s")
            raise TimeoutException(
                f"Cant find element={element} for the timeout={timeout}s"
            )
        return True
