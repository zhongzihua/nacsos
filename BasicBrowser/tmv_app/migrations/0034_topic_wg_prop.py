# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0033_topic_primary_wg'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='wg_prop',
            field=models.FloatField(null=True),
        ),
    ]
