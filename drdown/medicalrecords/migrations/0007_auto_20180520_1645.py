# Generated by Django 2.0.3 on 2018-05-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0006_medicine_medicine_use_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Time of complaint'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_in_use',
            field=models.BooleanField(default=True, help_text='Does the patient still use this medication?', verbose_name='In use?'),
        ),
    ]
