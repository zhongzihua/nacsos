# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0002_auto_20161011_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='gensim_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
