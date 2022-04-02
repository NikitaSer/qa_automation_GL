import requests

link = 'https://catfact.ninja/fact'


def get_request(url):
    response = requests.get(url=url)
    response_status_code = response.status_code
    response_body = response.text

    print(f'Status code: {response_status_code}\nResponse body: {response_body}')


if __name__ == '__main__':
    get_request(link)
