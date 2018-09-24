from django.db import models
from django.core.exceptions import ValidationError


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'Instagram account: {self.username}'
    
    def save(self, *args, **kwargs):
        if Account.objects.count() == 1:
            raise ValidationError('Can only have one account!')
        super(Account, self).save(*args, **kwargs)
