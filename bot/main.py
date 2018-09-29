"""
Main bot function.
Runs a infinite while loop
selects 'jobs' functions at random every 2 to 5 minutes
"""
import time
import datetime
from random import choice

from account.models import AccountActions
from .models import Hashtag
from .browser import chrome_browser
from .account.actions import login
from .jobs.hashtag_search import run as run_hashtag_search

def run():

    # Actions per day count
    account_actions, created = AccountActions.objects.get_or_create(
        day=datetime.datetime.now()
    )

    browser = chrome_browser()
    login(browser)

    while True:
        # Jobs in this list need to be checked agains an action
        # counter before they can run
        action_jobs = [
            'run_hashtag_search',
        ]

        # All Jobs
        job_options = [
            'run_hashtag_search',
        ]

        hashtag = choice(Hashtag.objects.all())
        random_job = choice(job_options)

        # TODO: refactor this, with function, times, and colors
        if random_job in action_jobs:
            if account_actions.can_perform_actions:
                print(f'Starging job {random_job}')
                eval(f'{random_job}(browser,"{hashtag.name}", 2)')
                print(f'Ended job {random_job}')  
        else:
            print(f'Starging job {random_job}')
            eval(f'{random_job}(browser,"{hashtag.name}", 2)')
            print(f'Ended job {random_job}')

        sleep_time = choice(range(120, 300))
        print(f'Going to sleep for {sleep_time} seconds')
        time.sleep(sleep_time)

