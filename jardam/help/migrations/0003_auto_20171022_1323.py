# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0002_auto_20171021_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='Описание'),
        ),
    ]
