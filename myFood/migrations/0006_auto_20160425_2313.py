# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0005_auto_20160425_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ean_code',
            field=models.CharField(blank=True, default=None, max_length=13),
        ),
    ]