# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-09 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0092_doc_tilength'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipccref',
            name='chapter',
            field=models.TextField(null=True),
        ),
    ]