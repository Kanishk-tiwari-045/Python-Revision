# Generated by Django 5.0.6 on 2024-06-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
