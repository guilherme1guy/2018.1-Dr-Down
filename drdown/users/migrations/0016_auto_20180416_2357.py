# Generated by Django 2.0.3 on 2018-04-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20180416_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_team',
            name='council_acronym',
            field=models.CharField(choices=[('CRM', 'CRM'), ('CRP', 'CRP'), ('COFFITO', 'COFFITO')], help_text='The Regional Council.', max_length=30, verbose_name='Council Acronym'),
        ),
        migrations.AlterField(
            model_name='health_team',
            name='registration_state',
            field=models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], help_text='The registration state of member of health team.', max_length=30, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='health_team',
            name='speciality',
            field=models.CharField(choices=[('Speech Therapy', 'Speech Therapy'), ('Occupational Therapy', 'Occupational Therapy'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Psychology', 'Psychology'), ('Physiotherapy', 'Physiotherapy'), ('Doctor', 'Doctor')], help_text='The speciality that this member of health team works.', max_length=30, verbose_name='Speciality'),
        ),
    ]
