# Generated by Django 5.0.6 on 2024-06-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='techstack',
            field=models.CharField(default='Django', max_length=100),
            preserve_default=False,
        ),
    ]
