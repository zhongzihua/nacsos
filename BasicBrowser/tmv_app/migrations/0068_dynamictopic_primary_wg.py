# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0067_dynamictopic_ipcc_coverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamictopic',
            name='primary_wg',
            field=models.IntegerField(null=True),
        ),
    ]