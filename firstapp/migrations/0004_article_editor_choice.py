# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20170217_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='editor_choice',
            field=models.BooleanField(default=False),
        ),
    ]