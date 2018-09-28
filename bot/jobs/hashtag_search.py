"""
    1. Goes to the hastag page
    2. Clicks on the first post (not from the most popular)
    3. Likes the post
    4. Leaves a comment
    5. For now follows untill we are following 2000 people
    6. Returns True
"""
import time
from selenium.webdriver.common.keys import Keys

from .utils import random_comment
from bot.models import User


def run(browser, hashtag, sleep):
    
    # Go to hashtag page
    browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

    # Click on first post (not from the most popular)
    a = browser.find_elements_by_tag_name('a')[10]
    a.click()
    time.sleep(sleep)

    post = browser.find_element_by_xpath('//div[@role="dialog"]')
    buttons = post.find_elements_by_tag_name('button')

    # Likes the post
    buttons[1].find_element_by_tag_name('span').click()
    time.sleep(sleep)

    # Leaves a comment
    textarea = post.find_element_by_tag_name('textarea')
    textarea.send_keys(random_comment(hashtag))
    textarea.send_keys(Keys.ENTER)
    time.sleep(sleep)

    # Follows
    if User.objects.count() > 2000:
        return True
    
    buttons[0].click()
    time.sleep(sleep)

    return True
