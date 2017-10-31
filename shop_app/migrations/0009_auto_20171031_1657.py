# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_auto_20171030_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='feed',
            new_name='feeds',
        ),
        migrations.AddField(
            model_name='feed',
            name='animals',
            field=models.ManyToManyField(to='shop_app.Animal'),
        ),
    ]