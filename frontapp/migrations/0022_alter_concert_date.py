# Generated by Django 4.1.7 on 2023-03-05 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0021_alter_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 5, 50, 9, 925474), verbose_name='Concert Date'),
        ),
    ]