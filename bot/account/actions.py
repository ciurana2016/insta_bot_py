import time
from selenium.webdriver.common.keys import Keys

from account.models import Account


def login(browser):
    LOGIN_URL = 'https://www.instagram.com/accounts/login/'
    FINAL_URL = 'https://www.instagram.com/'

    account = Account.objects.first()

    browser.get(LOGIN_URL)
    username_input = browser.find_element_by_name('username')
    username_input.send_keys(account.username)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys(account.password)
    password_input.send_keys(Keys.ENTER)

    # If instagram asks us to "save details" we say ok
    while FINAL_URL != browser.current_url:
        if 'onetap' in browser.current_url:
            time.sleep(1)
            browser.find_element_by_tag_name('button').click()

    return True
