# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-26 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0088_wosarticle_wc'),
    ]

    operations = [
        migrations.CreateModel(
            name='WC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('doc', models.ManyToManyField(to='scoping.Doc')),
            ],
        ),
    ]