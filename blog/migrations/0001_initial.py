# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver1', models.CharField(max_length=80)),
                ('ver2', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver3', models.CharField(max_length=80)),
            ],
        ),
    ]
