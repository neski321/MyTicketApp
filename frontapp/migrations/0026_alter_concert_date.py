# Generated by Django 4.1.7 on 2023-03-05 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0025_alter_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 6, 53, 33, 234757), verbose_name='Concert Date'),
        ),
    ]
