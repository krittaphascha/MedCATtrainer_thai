# Generated by Django 2.2.9 on 2020-01-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_annotatedentity_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectannotateentities',
            name='train_model_on_submit',
            field=models.BooleanField(default=True),
        ),
    ]