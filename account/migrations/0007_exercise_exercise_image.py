# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_workout_workout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]