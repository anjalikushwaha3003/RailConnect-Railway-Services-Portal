# Generated by Django 5.0.4 on 2024-05-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_train_delete_ticketbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='RailwayStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=255)),
                ('station_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Train',
        ),
    ]
