import os
import time
from selenium import webdriver

## Just to check the chrome driver (will delete this later)

chromedriver = os.getcwd() + '/chromedriver'

# User goes to google on his iPad
mobile_emulation = {'deviceName': 'iPad'}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)

# User goes incognito and without infobars (they show mesage like= you a bot)
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--incognito')

browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
browser.set_window_size(768, 1024)

browser.get('https://google.com')

# User goes to instagram after 1 second of Googling
time.sleep(1)
browser.get('https://instagram.com/accounts/login/')

# User is stupid wonders 2 seconds on screen and closes broser
# time.sleep(2)
# browser.close()
