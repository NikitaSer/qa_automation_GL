import requests
from framework.tools.utils import form_url


class BaseRequests:
    """Class for calling HTTP requests"""

    def __init__(self):
        self.token = None
        self.headers = None

    def set_token(self, token):
        """Method for setting token to the object and relevant header"""
        self.token = token
        self.headers = {"x-token": token}

    def form_headers(self, headers):
        if headers is None:
            headers = {}
        if self.headers is None:
            self.headers = {}
        headers = {**self.headers, **headers}
        return headers

    def get(self, url, headers=None, *args, **kwargs):
        """Reimplementation of GET method"""
        url = form_url(url=url)
        headers = self.form_headers(headers)
        return requests.get(url=url, headers=headers, *args, **kwargs)

    def post(self, url, headers=None, *args, **kwargs):
        """Reimplementation of POST method"""
        url = form_url(url=url)
        headers = self.form_headers(headers)
        return requests.post(url=url, headers=headers, *args, **kwargs)
