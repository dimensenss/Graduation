# Generated by Django 4.2.16 on 2024-09-24 16:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_remove_courseinfo_preview_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='workload',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
