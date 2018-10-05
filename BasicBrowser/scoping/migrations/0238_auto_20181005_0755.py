# Generated by Django 2.0.5 on 2018-10-05 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0237_query_queries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Technology',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='docpar',
            old_name='technology',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='docstatement',
            old_name='technology',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='technology',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='snowballingsession',
            old_name='technology',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='technology',
        ),
        migrations.AlterField(
            model_name='docownership',
            name='relevant',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Yes'), (2, 'No'), (3, 'Maybe'), (4, 'Other Category'), (5, 'Tech Relevant & Innovation Relevant'), (6, 'Tech Relevant & Innovation Irrelevant'), (7, 'Tech Irrelevant & Innovation Relevant'), (8, 'Tech Irrelevant & Innovation Irrelevant'), (9, 'Badly Parsed')], db_index=True, default=0, verbose_name='Relevance'),
        ),
    ]
