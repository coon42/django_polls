# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0003_auto_20160425_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ean_code',
            field=models.CharField(default=False, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='is_fluid',
            field=models.BooleanField(default=False),
        ),
    ]
