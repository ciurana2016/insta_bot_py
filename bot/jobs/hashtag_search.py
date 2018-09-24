import requests
from bs4 import BeautifulSoup


def get_response(hashtag):
    r = requests.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    if r.status_code == 200:
        return r.text
    else:
        return r.status_code


def main(browser, actions):
    pass