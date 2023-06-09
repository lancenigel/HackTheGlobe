# Generated by Django 4.1.7 on 2023-03-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('ethnicity', models.CharField(choices=[('Hispanic', 'Hispanic'), ('White ', 'White'), ('Black', 'Black'), ('Asian', 'Asian'), ('Other', 'Other')], max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('contact_method', models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], default='phone', max_length=5)),
                ('athlete_image', models.ImageField(null=True, upload_to='athletes/')),
            ],
        ),
    ]
