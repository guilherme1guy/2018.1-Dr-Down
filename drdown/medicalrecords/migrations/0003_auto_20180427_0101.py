# Generated by Django 2.0.3 on 2018-04-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0002_auto_20180426_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='document',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
