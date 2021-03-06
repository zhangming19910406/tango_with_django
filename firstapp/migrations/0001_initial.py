# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('img', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('avatar', models.CharField(default='http://semantic-ui.com/images/avatar/small/matt.jpg', max_length=100)),
                ('content', models.TextField()),
                ('create_time', models.DateField(auto_now=True)),
                ('belong_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='under_comment', to='firstapp.Article')),
            ],
        ),
    ]
