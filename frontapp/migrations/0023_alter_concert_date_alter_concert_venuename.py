# Generated by Django 4.1.7 on 2023-03-05 11:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0022_alter_concert_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 6, 31, 14, 649804), verbose_name='Concert Date'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venueName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontapp.venueowner', verbose_name='Venue'),
        ),
    ]
