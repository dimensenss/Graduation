# Generated by Django 4.2.16 on 2024-09-16 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_teacher',
        ),
    ]
