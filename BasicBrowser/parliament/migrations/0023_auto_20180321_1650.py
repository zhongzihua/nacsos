# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0022_auto_20180321_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituency',
            name='has_coal',
            field=models.NullBooleanField(),
        ),
    ]