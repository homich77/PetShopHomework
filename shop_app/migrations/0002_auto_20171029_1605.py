# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='book',
            new_name='animal',
        ),
    ]
