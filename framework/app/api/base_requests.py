import requests
from config.config import Config


class BaseRequests:
    """Class for calling HTTP requests"""
    
    def __init__(self):
        self.token = None
        self.headers = None
    
    def set_token(self, token):
        self.token = token
        self.headers = {'x-token': token}
    
    def form_url(self, url):
        """Method to concat base url and api path"""
        return Config.BASE_URL + url

    def get(self, url, *args, **kwargs):
        """Reimplementation of GET method"""
        url = self.form_url(url=url)
        headers = MERGER TWO DICT. headers and self.headers
        return requests.get(url=url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        """Reimplementation of POST method"""
        url = self.form_url(url=url)
        return requests.post(url=url, *args, **kwargs)
