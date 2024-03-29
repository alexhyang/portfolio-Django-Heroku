# Generated by Django 3.2.4 on 2021-07-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0003_rename_settings_setting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='card_title_uppercase',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='short_definition',
        ),
        migrations.AddField(
            model_name='setting',
            name='word_definition',
            field=models.CharField(default='short', max_length=16),
        ),
        migrations.AddField(
            model_name='setting',
            name='word_title_case',
            field=models.CharField(default='normal', max_length=16),
        ),
    ]
