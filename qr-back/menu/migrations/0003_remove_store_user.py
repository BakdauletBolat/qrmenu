# Generated by Django 5.0.1 on 2024-02-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='user',
        ),
    ]
