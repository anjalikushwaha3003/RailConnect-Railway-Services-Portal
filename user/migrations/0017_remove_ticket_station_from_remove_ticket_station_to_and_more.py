# Generated by Django 5.0.4 on 2024-05-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_remove_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='station_from',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='station_to',
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
