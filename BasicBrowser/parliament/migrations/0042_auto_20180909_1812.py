# Generated by Django 2.0.5 on 2018-09-09 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0041_auto_20180909_1810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoleType',
            new_name='SpeakerRole',
        ),
    ]
