# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-20 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_profile',
            field=models.IntegerField(default=0),
        ),
    ]