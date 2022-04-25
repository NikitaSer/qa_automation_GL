import requests
from config.config import Config


class BaseRequests:
    """Class for calling HTTP requests"""

    def form_url(self, url):
        """Method to concat base url and api path"""
        return Config.BASE_URL + url

    def get(self, path, headers):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        return requests.get(url=url, headers=headers)

    def post(self, path, headers):
        url = self.form_url(path)
        return requests.post(url=url, headers=headers)
