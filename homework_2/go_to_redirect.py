import requests

url_with_redirect = "https://tinyurl.com/yc2ta8fw"


def get_location_header_url(url):
    response = requests.head(url=url)
    response_headers = response.headers
    location_header_url = response_headers["location"]
    return location_header_url


def get_request(url):
    response = requests.get(url=url)
    response_status_code = response.status_code
    response_body = response.text
    print(f'Status code: {response_status_code}\nResponse body: {response_body}')


if __name__ == "__main__":
    url_without_redirect = get_location_header_url(url_with_redirect)
    get_request(url_without_redirect)
