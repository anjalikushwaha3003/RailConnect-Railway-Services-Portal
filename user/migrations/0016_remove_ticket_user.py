# Generated by Django 5.0.4 on 2024-05-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_ticket_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]