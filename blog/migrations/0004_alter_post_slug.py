# Generated by Django 4.2.6 on 2024-01-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, unique_for_date='publish'),
        ),
    ]
