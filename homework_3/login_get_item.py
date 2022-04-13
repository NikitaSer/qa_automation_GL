import requests
from properties import LOGIN_LINK, GET_ITEM_LINK, TEST_USER, ITEM_ID


def user_login(user):
    response_ = requests.post(LOGIN_LINK, json={'username': user.username, 'password': user.password})
    response_json = response_.json()
    access_token = response_json['access_token']
    refresh_token = response_json['refresh_token']
    user.access_token = access_token
    user.refresh_token = refresh_token


def get_item(item_id, user):
    specific_item_link = GET_ITEM_LINK + f'/{item_id}'
    response_ = requests.get(specific_item_link, headers={'Authorization': f'Bearer {user.access_token}'})
    response_text = response_.text
    print(response_text)


if __name__ == '__main__':
    user_login(user=TEST_USER)
    get_item(item_id=ITEM_ID, user=TEST_USER)
