# Generated by Django 2.0.5 on 2018-07-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0033_auto_20180711_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='text_source',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='information_source',
            field=models.TextField(default=''),
        ),
    ]
