# Generated by Django 4.2.6 on 2023-11-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_visit_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='max_speed',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]