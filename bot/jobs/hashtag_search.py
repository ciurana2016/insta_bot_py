"""
1. Goes to the hastag page
2. Clicks on the first post (not from the most popular)
3. Likes the post
4. Leaves a comment (33% chance of commenting [to be safe])
5. For now follows untill we are following 2000 people
6. Returns True
"""
import time
from random import choice
from selenium.webdriver.common.keys import Keys

from .utils import random_comment, follow_user
from bot.models import User


def like_and_comment(browser, hashtag, sleep):
    # Go to hashtag page
    browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

    # Click on first post (not from the most popular)
    a = browser.find_elements_by_tag_name('a')[10]
    a.click()
    time.sleep(sleep)

    post = browser.find_element_by_xpath('//div[@role="dialog"]')
    buttons = post.find_elements_by_tag_name('button')

    # If we have multiple images, remove the button for next pic
    potential_next_btn = buttons[1].get_attribute('tabindex')
    if potential_next_btn != None:
        buttons.pop(1)

    # Likes the post
    buttons[1].find_element_by_tag_name('span').click()
    time.sleep(sleep)

    # 33% Chance to leave a comment
    if choice([0,1,0]) == 1:
        textarea = post.find_element_by_tag_name('textarea')
        textarea.send_keys(random_comment(hashtag))
        textarea.send_keys(Keys.ENTER)
        time.sleep(sleep)


def run(browser, hashtag, sleep):
    
    like_and_comment(browser, hashtag, sleep)

    # Follows
    links = post.find_elements_by_tag_name('a')
    username = links[3].get_attribute('title')
    follow_user(browser, username)
    time.sleep(sleep)

    return True
