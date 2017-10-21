# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=255, verbose_name='Проблема')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('info', models.CharField(max_length=255, verbose_name='Информация')),
                ('contacts', models.CharField(max_length=255, verbose_name='Контакты')),
            ],
        ),
    ]