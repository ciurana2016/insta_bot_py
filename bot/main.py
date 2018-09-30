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

    browser = chrome_browser()
    login(browser)

    while True:

        # Actions per day count, prevents infinite actions
        account_actions, created = AccountActions.objects.get_or_create(
            day=datetime.datetime.now()
        )

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

        if random_job in action_jobs:
            if account_actions.can_perform_actions:
                account_actions.actions += 1
                account_actions.save()
                start_job(browser, random_job, hashtag.name)
        else:
            start_job(browser, random_job, hashtag.name)

        # Goes to sleep for a random amount of time
        random_sleep()


def random_sleep():
    sleep_interval = 10
    sleep_time = choice(range(120, 200))
    remaining_time = sleep_time
    print(f'Going to sleep for {sleep_time} seconds')
    for stop in range(sleep_time//sleep_interval):
        time.sleep(sleep_interval)
        remaining_time -= sleep_interval
        print(f'\t{remaining_time} seconds to start again ...')


def start_job(browser, job_name, hashtag):
    print(f'Starging job {job_name}')
    eval(f'{job_name}(browser,"{hashtag}", 2)')
    print(f'Ended job {job_name}')