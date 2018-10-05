# Generated by Django 2.0.5 on 2018-09-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0227_auto_20180913_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyeffect',
            name='intervention_start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='baseline_consumption',
            field=models.TextField(blank=True, help_text='kWh/year', null=True),
        ),
    ]