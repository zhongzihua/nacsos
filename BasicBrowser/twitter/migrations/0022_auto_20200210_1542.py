# Generated by Django 2.2.9 on 2020-02-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0021_twittersearch_search_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterbasemodel',
            name='created_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]