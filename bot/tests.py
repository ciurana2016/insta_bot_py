import time
from bs4 import BeautifulSoup
from django.test import TestCase

from .browser import chrome_browser
from .account.actions import login
from .jobs import hashtag_search
from .jobs.utils import random_comment, follow_user, unfollow_user

from .models import User, Hashtag
from account.models import Account


class BrowserWorksTest(TestCase):

    def setUp(self):
        self.browser = chrome_browser()

    def tearDown(self):
        self.browser.quit()

    def test_browser_works(self):
        self.browser.get('https://google.com')
        self.assertEqual(self.browser.title, 'Google')

    def test_account_can_log_in(self):
        self.assertTrue(login(self.browser))


class BotModelsTest(TestCase):

    def test_saving_and_retrieving_users(self):
        user_one = User()
        user_one.name = 'test name one'
        user_one.id = '12345645653498534'
        user_one.following = False
        user_one.save()
        self.assertFalse(user_one.following)
        user_one.following = True
        user_one.save()
        self.assertTrue(user_one.following)

    def test_save_and_retireve_hashtags(self):
        my_hashtags = ['dogs', 'cats', 'birds']

        h1 = Hashtag.objects.create(name='dogs')
        h2 = Hashtag.objects.create(name='cats')
        h3 = Hashtag.objects.create(name='birds')
        self.assertEqual(3, Hashtag.objects.count())

        for hashtag in Hashtag.objects.all():
            self.assertIn(hashtag.name, my_hashtags)


class BotUtilsTest(TestCase):

    def setUp(self):
        self.browser = chrome_browser()
        login(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_random_comment(self):
        comment = random_comment('test')
        valid_choices = [
            'Yeah test rocks!',
            'Nice!',
            '#test !',
            'yup',
            'so true'
        ]
        self.assertIn(comment, valid_choices)
    
    def test_follow_unfollow_users(self):
        followed_users_count = User.objects.count()
        followed = follow_user(self.browser, 'lacteosdiqueno')

        self.assertTrue(followed)
        self.assertTrue(User.objects.count() > followed_users_count)

        # Check cant follow already followed user
        follow = follow_user(self.browser, 'lacteosdiqueno')
        self.assertFalse(follow)

        # Check can unfollow users correctly
        followed_users_count = User.objects.count()
        unfollow = unfollow_user(self.browser, 'lacteosdiqueno')
        unfollowed_user = User.objects.get(name='lacteosdiqueno')
        self.assertTrue(unfollow)
        self.assertTrue(unfollowed_user.following == False)
    

class HashtagSearchJobTest(TestCase):

    def test_hashtag_search_job(self):

        browser = chrome_browser()
        login(browser)
        test_hashtag = 'programmers'

        # Bot goes to hastag page and clicks on a post
        hashtag_search.run(browser, test_hashtag, 0.5)

        # Check the bot went to a post page
        self.assertIn('/p/', browser.current_url)
        self.assertIn(f'/?tagged={test_hashtag}', browser.current_url)

        post = browser.find_element_by_xpath('//div[@role="dialog"]')
        buttons = post.find_elements_by_tag_name('button')

        # If we have multiple images, remove the button for next pic
        potential_next_btn = buttons[1].get_attribute('tabindex')
        if potential_next_btn != None:
            buttons.pop(1)

        # Check the bot liked the post
        heart_element = buttons[1].find_element_by_tag_name('span')
        self.assertIn('filled', heart_element.get_attribute('class'))

        # Check the bot posted a comment
        # First has to check if the textarea is not disabled
        while post.find_element_by_tag_name('textarea').get_attribute('disabled'):
            print('Textarea is disabled, I\'m waiting ...')
            time.sleep(0.5)

        account = Account.objects.first()
        comments = post.find_elements_by_class_name('notranslate')

        self.assertIn(
            account.username,
            [comment.get_attribute('title') for comment in comments]
        )

        # Aseume the bot followed correctly (this is tested elsewhere)
        browser.quit()
