# Generated by Django 4.1.7 on 2023-03-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0005_alter_athlete_blood_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='athlete_image',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
