import datetime

from django.db import models


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    following = models.BooleanField(default=False)
    followed_from = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'@{self.name}'


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'#{self.name}'
