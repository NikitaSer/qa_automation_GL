import logging
from app.api.base_requests import BaseRequests
from app.api.urls import Urls
from config.config import Config
from app.api.errors import AccessTokenIsMissed


class ApiClient(BaseRequests):
    """Class implementing API methods"""

    def login(self):
        """Method for user's login"""
        r = self.post(url=Urls.LOGIN, headers={"Authorization": Config.LOGIN_TOKEN})
        r.raise_for_status()
        token = r.json().get("token")
        if token is None:
            logging.error("Cannot get token from login request.")
            raise AccessTokenIsMissed("Cannot get token from login request.")
        self.set_token(token)

    def get_files_in_root(self):
        """Method to receive info about files in root folder"""
        r = self.get(url=Urls.FILES_V2)
        return r.json()

    def get_files_in_specific_folder(self, folder_id):
        """Method to receive info about files in a specific folder"""
        r = self.get(url=Urls.FILES_V2, params={"file_id": folder_id})
        return r.json()

    def get_count_files_in_specific_folder(self, folder_id):
        """Method to receive number of files in a specific folder"""
        r = self.get(url=Urls.FILES_COUNT, params={"file_id": folder_id})
        return r.json()

    def get_runs_for_specific_file(self, file_id):
        """Method to receive number of runs in a specific folder"""
        r = self.get(url=Urls.FILE_RESULT_GET_RUN.format(file_id))
        return r.json()

    def get_analysis_for_specific_run(self, run_id):
        """Method to receive number of analysis for a specific run"""
        r = self.get(url=Urls.FILE_RESULT_GET_ANALYSIS.format(run_id))
        return r.json()

    def get_artifacts_for_specific_run(self, run_id):
        """Method to receive number of artifacts for a specific run"""
        r = self.get(url=Urls.FILE_RESULT_GET_ARTIFACT.format(run_id))
        return r.json()
