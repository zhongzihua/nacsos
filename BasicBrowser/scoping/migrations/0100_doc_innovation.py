# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-19 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0099_auto_20170512_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='innovation',
            field=models.ManyToManyField(db_index=True, to='scoping.Innovation'),
        ),
    ]