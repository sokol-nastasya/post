# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-26 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_post', '0007_auto_20181126_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
