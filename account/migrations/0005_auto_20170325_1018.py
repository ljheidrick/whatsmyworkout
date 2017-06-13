# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170325_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workouts',
            field=models.ManyToManyField(to='account.Workout'),
        ),
    ]
