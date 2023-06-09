# Generated by Django 4.1.7 on 2023-03-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0004_athlete_blood_type_athlete_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=4, null=True),
        ),
    ]
