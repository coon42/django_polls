# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0009_auto_20160426_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='container_types',
            field=models.ManyToManyField(through='myFood.Packages', to='myFood.ContainerType'),
        ),
    ]
