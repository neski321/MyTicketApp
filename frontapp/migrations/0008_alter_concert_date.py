# Generated by Django 4.1.7 on 2023-03-05 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0007_alter_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 2, 38, 58, 447817), verbose_name='Concert Date'),
        ),
    ]
