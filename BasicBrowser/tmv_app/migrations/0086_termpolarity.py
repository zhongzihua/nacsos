# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-27 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0085_doctopic_par'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermPolarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polarity', models.FloatField()),
                ('source', models.TextField()),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmv_app.Term')),
            ],
        ),
    ]