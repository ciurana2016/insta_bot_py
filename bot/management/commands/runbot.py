from django.core.management.base import BaseCommand, CommandError

from bot.main import run as runbot

class Command(BaseCommand):
    help = 'Executes bot/main.py run()'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print('Command start')
        runbot()
        print('Command ended')