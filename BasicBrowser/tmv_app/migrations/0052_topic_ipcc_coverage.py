# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0051_topicarscores_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='ipcc_coverage',
            field=models.FloatField(null=True),
        ),
    ]