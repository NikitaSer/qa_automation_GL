import requests
from config.config import Config


class BaseRequests:
    """Class for calling HTTP requests"""

    def form_url(self, url):
        """Method to concat base url and api path"""
        return Config.BASE_URL + url

    def get(self, url, *args, **kwargs):
        """Reimplementation of GET method"""
        url = self.form_url(url=url)
        logger.debug(f"Request: {url} will be send now")
        return requests.get(url=url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        """Reimplementation of POST method"""
        url = self.form_url(url=url)
        return requests.post(url=url, *args, **kwargs)
