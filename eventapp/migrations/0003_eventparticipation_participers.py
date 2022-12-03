# Generated by Django 4.1.3 on 2022-12-03 00:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventapp', '0002_eventparticipation'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipation',
            name='participers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
