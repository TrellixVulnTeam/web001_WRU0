# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-24 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]