# Generated by Django 4.1.7 on 2023-03-19 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athlete', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to=settings.AUTH_USER_MODEL),
        ),
    ]