# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-14 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0002_auto_20180614_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='pais',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
