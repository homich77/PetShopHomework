# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_auto_20171031_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(default='dog', max_length=10),
        ),
    ]
