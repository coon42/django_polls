# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='nutritions',
            field=models.ManyToManyField(through='myFood.Composition', to='myFood.Nutrition'),
        ),
        migrations.AddField(
            model_name='composition',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFood.Food'),
        ),
        migrations.AddField(
            model_name='composition',
            name='nutrition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myFood.Nutrition'),
        ),
    ]
