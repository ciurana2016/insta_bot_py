import datetime

from django.db import models
from django.core.exceptions import ValidationError


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'Instagram account: {self.username}'
    
    def get_limit(self):
        """
        Calculates amount of actions this account can perform every day
        depending on how old the account is
        """
        base_actions = 65
        today = datetime.datetime.now()
        days_since_creation = (today - self.created).days
        base_actions += days_since_creation * 15 if days_since_creation < 33 else 435
        return base_actions

    def save(self, *args, **kwargs):
        oneaccount = Account.objects.first()
        if Account.objects.count() == 1 and oneaccount.username != self.username:
            raise ValidationError('Can only have one account!')
        super(Account, self).save(*args, **kwargs)


class AccountActions(models.Model):
    day = models.DateField(default=datetime.date.today)
    actions = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.actions} performed on day {self.day}'
    
    def can_perform_actions(self, limit):
        self.actions +=1
        self.save()
        return True if self.actions < limit else False