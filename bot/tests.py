from django.test import TestCase

from .browser import chrome_browser
from .account.actions import login


class TestBrowserWorks(TestCase):

    def setUp(self):
        self.browser = chrome_browser()

    def tearDown(self):
        self.browser.quit()

    def test_browser_works(self):
        self.browser.get('https://google.com')
        self.assertEqual(self.browser.title, 'Google')

    def test_account_can_log_in(self):
        self.assertTrue(login(self.browser))