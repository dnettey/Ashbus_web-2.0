# Generated by Django 3.2 on 2021-04-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashbus_web', '0003_remove_driver_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='ratings',
        ),
    ]
