# Generated by Django 5.0.6 on 2024-05-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0008_mycontact_othercontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='myDiscription',
            field=models.TextField(max_length=500),
        ),
    ]
