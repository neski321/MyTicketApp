# Generated by Django 4.1.7 on 2023-03-06 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0037_alter_ticketorder_seat_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='seats1_avail',
            new_name='seats_avail1',
        ),
        migrations.RenameField(
            model_name='concert',
            old_name='seats2_avail',
            new_name='seats_avail2',
        ),
        migrations.RenameField(
            model_name='concert',
            old_name='seats3_avail',
            new_name='seats_avail3',
        ),
        migrations.RenameField(
            model_name='concert',
            old_name='seats4_avail',
            new_name='seats_avail4',
        ),
        migrations.RenameField(
            model_name='venueowner',
            old_name='num1',
            new_name='seats_avail1',
        ),
        migrations.RenameField(
            model_name='venueowner',
            old_name='num2',
            new_name='seats_avail2',
        ),
        migrations.RenameField(
            model_name='venueowner',
            old_name='num3',
            new_name='seats_avail3',
        ),
        migrations.RenameField(
            model_name='venueowner',
            old_name='num4',
            new_name='seats_avail4',
        ),
    ]
