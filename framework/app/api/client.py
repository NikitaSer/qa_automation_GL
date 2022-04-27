import logging
from app.api.base_requests import BaseRequests
from app.api.urls import Urls
from config.config import Config
from app.api.errors import AccessTokenIsMissed


class ApiClient(BaseRequests):
    """Class implementing API methods"""

    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method for user's login"""
        r = self.post(url=Urls.LOGIN, headers={'Authorization': Config.LOGIN_TOKEN})
        r.raise_for_status()
        token = r.json().get('token')
        if token is None:
            logging.error('Cannot get token from login request.')
            raise AccessTokenIsMissed('Cannot get token from login request.')
        self.token = token

    def get_files_in_root(self):
        """Method to receive info about files in root folder"""
        r = self.get(url=Urls.FILES_IN_ROOT, headers={'x-token': self.token})
        r.raise_for_status()

    def get_files_in_specific_folder(self):
        """Method to receive info about files in a specific folder"""
        r = self.get(url=Urls.FILES_IN_SPECIFIC_FOLDER, headers={'x-token': self.token})
        r.raise_for_status()

    def get_count_files_in_specific_folder(self):
        """Method to receive number of files in a specific folder"""
        r = self.get(url=Urls.COUNT_FILES, headers={'x-token': self.token})
        r.raise_for_status()
