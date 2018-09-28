import time
from random import choice

from django.core.exceptions import ObjectDoesNotExist

from bot.models import User


def random_comment(hashtag):
    choices = [
        f'Yeah {hashtag} rocks!',
        'Nice!',
        f'#{hashtag} !',
        'yup',
        'so true'
    ]
    return choice(choices)


def follow_user(browser, username):
    if User.objects.count() >= 7500:
        return False

    try:
        u = User.objects.get(name=username)
        return False
    except ObjectDoesNotExist:
        pass

    browser.get(f'https://instagram.com/{username}/')
    buttons = browser.find_elements_by_tag_name('button')
    buttons[0].click()

    User.objects.create(name=username, following=True)
    return True


def unfollow_user(browser, username):
    browser.get(f'https://instagram.com/{username}/')
    buttons = browser.find_elements_by_tag_name('button')
    buttons[0].click()
    time.sleep(0.5)
    presentation = browser.find_element_by_xpath('//div[@role="presentation"]')
    unfollow_button = presentation.find_elements_by_tag_name('button')[1]
    unfollow_button.click()
    user = User.objects.get(name=username)
    user.following = False
    user.save()
    return True
