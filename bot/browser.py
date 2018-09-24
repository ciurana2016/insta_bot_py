import os
from selenium import webdriver


def chrome_browser():
    """
    Returns a browser object (Chrome) 
    """
    chromedriver = os.getcwd() + '/chromedriver'

    mobile_emulation = {'deviceName': 'iPad'}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)

    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--incognito')

    browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    browser.set_window_size(768, 1024)

    return browser
