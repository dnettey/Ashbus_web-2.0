# Generated by Django 3.2 on 2021-04-16 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashbus_web', '0002_alter_trip_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='bus',
        ),
    ]
