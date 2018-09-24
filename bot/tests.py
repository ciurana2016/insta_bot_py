from bs4 import BeautifulSoup
from django.test import TestCase

from .browser import chrome_browser
from .account.actions import login
from .jobs import hashtag_search

from .models import User, Hashtag


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


class HashtagSearchJobTest(TestCase):

    # TODO: need to read on mocks, cause I cant be making real requests
    # to test logic, or Im doing something wrong

    def test_scraping_returns_what_we_are_looing_for(self):
        html = hashtag_search.get_response('programming')
        soup = BeautifulSoup(html, 'html.parser')
        self.assertIn('programming', str(soup.title))

    def test_like_on_posts(self):
        html = '<html></html>'
        liked = hashtag_search.like_post(html, 5)
        self.assertTrue(liked)
    
    def test_coments_on_posts(self):
        pass
    
    def test_follows_users_not_followed_yet(self):
        pass