# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-27 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0005_auto_20180627_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
