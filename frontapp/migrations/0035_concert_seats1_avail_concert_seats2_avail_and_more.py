# Generated by Django 4.1.7 on 2023-03-06 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontapp', '0034_alter_concert_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='seats1_avail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='concert',
            name='seats2_avail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='concert',
            name='seats3_avail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='concert',
            name='seats4_avail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketorder',
            name='seat_type',
            field=models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Seat Tier'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venueName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontapp.venueowner', verbose_name='Venue'),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='concertName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontapp.concert', verbose_name='Concert'),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
