import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Account, AccountActions


class TestAccountModel(TestCase):

    def test_can_only_create_one_account(self):
        second_account = Account()
        second_account.username = 'test_username'
        second_account.passwords = 'test_password'
        
        with self.assertRaises(ValidationError) as error:
            second_account.save()

        self.assertTrue('Can only have one account!' in str(error.exception))
        
    def test_calculates_action_limit(self):
        account = Account.objects.first()
        account.created = datetime.datetime.now()
        account.save()
        self.assertTrue(account.get_limit() == 65)

        account.created = datetime.datetime.now() - datetime.timedelta(days=1)
        account.save()
        self.assertTrue(account.get_limit() == 80)

        account.created = datetime.datetime.now() - datetime.timedelta(days=5)
        account.save()
        self.assertTrue(account.get_limit() == 140)

        account.created = datetime.datetime.now() - datetime.timedelta(days=300)
        account.save()
        self.assertTrue(account.get_limit() == 500)


class TestAccountAcctionsCountModel(TestCase):

    def test_account_can_perform_actions(self):
        account_actions = AccountActions.objects.create(
            day= datetime.datetime.now(),
            actions=10
        )
        self.assertTrue(account_actions.can_perform_actions(65))

    
    def test_account_CANT_perform_more_actions(self):
        account_actions = AccountActions.objects.create(
            day= datetime.datetime.now(),
            actions=70
        )
        self.assertFalse(account_actions.can_perform_actions(70))