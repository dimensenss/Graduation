# Generated by Django 4.2.16 on 2024-09-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_alter_courseinfo_preview_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodules',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
