# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20171029_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='authors',
            new_name='feed',
        ),
    ]
