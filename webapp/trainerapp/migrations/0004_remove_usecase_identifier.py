# Generated by Django 2.2 on 2019-04-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0003_usecase_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usecase',
            name='identifier',
        ),
    ]