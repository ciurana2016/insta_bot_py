from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Account


class TestAccountModel(TestCase):

    def test_can_only_create_one_account(self):
        first_account = Account()
        first_account.username = 'test_username'
        first_account.passwords = 'test_password'
        first_account.save()
        
        with self.assertRaises(ValidationError) as error:
            second_account = Account()
            second_account.save()

        self.assertTrue('Can only have one account!' in str(error.exception))
        

