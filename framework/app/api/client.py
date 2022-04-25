import logging
from app.api.base_requests import BaseRequests
from app.api.urls import Urls
from config.config import Config
from app.api.errors import AccessTokenIsMissed


class ApiClient(BaseRequests):

    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r = self.post(path=Urls.LOGIN, headers={'Authorization': Config.LOGIN_TOKEN})
        token = r.json().get('token')
        if token is None:
            logging.error('Cannot get token from login request.')
            raise AccessTokenIsMissed('Cannot get token from login request.')
        self.token = token


    def get_folders(self):
        """Method to receive """
        r = self.get(path=Urls.ROOT_FOLDERS, headers={'x-token': self.token})
        r.raise_for_status()
