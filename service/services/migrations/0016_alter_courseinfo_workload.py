# Generated by Django 4.2.16 on 2024-09-24 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_alter_courseinfo_workload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='workload',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
