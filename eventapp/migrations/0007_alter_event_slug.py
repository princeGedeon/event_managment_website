# Generated by Django 4.1.3 on 2022-12-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0006_event_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]