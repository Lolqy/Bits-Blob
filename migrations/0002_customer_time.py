# Generated by Django 4.2.5 on 2024-06-22 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BNB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
