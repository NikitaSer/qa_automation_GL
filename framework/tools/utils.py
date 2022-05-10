import urllib
from framework.config.config import Config


def form_url(url):
    """Method to join base url and an api path"""
    return urllib.parse.urljoin(Config.BASE_URL, url)
