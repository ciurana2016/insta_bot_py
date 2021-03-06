# Generated by Django 2.1.1 on 2018-09-29 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('created', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='AccountActions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.date.today)),
                ('actions', models.IntegerField(default=0)),
            ],
        ),
    ]
