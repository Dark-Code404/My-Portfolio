# Generated by Django 5.0.6 on 2024-05-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0003_about_mydiscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='myDiscription',
            field=models.CharField(max_length=500),
        ),
    ]
