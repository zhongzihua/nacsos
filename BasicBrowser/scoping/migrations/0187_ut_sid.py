# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-23 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0186_auto_20180208_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='ut',
            name='sid',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Scopus_id'),
        ),
    ]
