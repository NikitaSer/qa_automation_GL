import requests
import os
import logging
from config.links import LOGIN_LINK, ROOT_FOLDER_LINK
from config.custom_errors import AccessTokenIsMissed


def login():
    response_ = requests.post(url=LOGIN_LINK,
                              headers={'Authorization': os.environ.get('AUTHORIZATION_VALUE')})
    token = response_.json().get('token')
    if token is None:
        logging.error('Cannot get token from login request.')
        raise AccessTokenIsMissed('Cannot get token from login request.')
    return token


def root_folder(token):
    response_ = requests.get(ROOT_FOLDER_LINK, headers={'x-token': token})
    logging.warning(response_.text)


if __name__ == '__main__':
    token = login()
    root_folder(token)
