# Generated by Django 5.0.6 on 2024-05-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0021_language_remove_resumeabout_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
            ],
        ),
    ]
