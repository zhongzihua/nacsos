# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-23 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0029_auto_20180323_1039'),
        ('tmv_app', '0083_auto_20180216_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='psearch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parliament.Search'),
        ),
    ]
