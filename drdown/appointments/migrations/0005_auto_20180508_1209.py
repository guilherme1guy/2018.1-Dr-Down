# Generated by Django 2.0.3 on 2018-05-08 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180507_1928'),
        ('appointments', '0004_request_day'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='AppointmentRequest',
        ),
    ]
