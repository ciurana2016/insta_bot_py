"""
Main bot function.
Runs a infinite while loop
selects 'jobs' functions at random every 2 to 5 minutes
"""
import time
from random import choice

from .models import Hashtag
from .browser import chrome_browser
from .account.actions import login
from .jobs.hashtag_search import run as run_hashtag_search

def run():

    browser = chrome_browser()
    login(browser)

    while True:

        job_options = [
            'run_hashtag_search',
        ]

        hashtag = choice(Hashtag.objects.all())

        random_job = choice(job_options)
        print(f'Starging job {random_job}')
        eval(f'{random_job}(browser,"{hashtag.name}", 0.5)')
        print(f'Ended job {random_job}')

        sleep_time = choice(range(120, 300))
        print(f'Going to sleep for {sleep_time} seconds')
        time.sleep(sleep_time)

