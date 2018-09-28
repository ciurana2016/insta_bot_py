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

    while FINAL_URL != browser.current_url:
        # If instagram asks us to "save details" we say ok
        if 'onetap' in browser.current_url:
            browser.find_element_by_tag_name('button').click()
            time.sleep(1)
        # If instagram asks to be isntalled we go to homepage
        if '#reactivated' in browser.current_url:
            browser.get(FINAL_URL)
            time.sleep(1)

    return True
