from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Account


class TestAccountModel(TestCase):

    def test_can_only_create_one_account(self):
        second_account = Account()
        second_account.username = 'test_username'
        second_account.passwords = 'test_password'
        
        with self.assertRaises(ValidationError) as error:
            second_account.save()

        self.assertTrue('Can only have one account!' in str(error.exception))
        

