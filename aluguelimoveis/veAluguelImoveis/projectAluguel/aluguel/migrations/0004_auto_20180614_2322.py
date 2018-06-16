# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-15 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_auto_20180614_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ('cidade',), 'verbose_name': 'imovel', 'verbose_name_plural': 'imoveis'},
        ),
        migrations.AlterField(
            model_name='imovel',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis', to='aluguel.Categoria'),
        ),
    ]
