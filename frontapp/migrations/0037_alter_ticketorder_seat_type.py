# Generated by Django 4.1.7 on 2023-03-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0036_alter_ticketorder_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketorder',
            name='seat_type',
            field=models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Seat Tier'),
        ),
    ]
