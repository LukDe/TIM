# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tim_app', '0004_remove_user_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='location',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='supply',
            name='location',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=128),
        ),
    ]
