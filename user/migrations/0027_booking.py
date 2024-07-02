# Generated by Django 4.2.7 on 2024-05-31 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('train_number', models.CharField(max_length=50)),
                ('class_type', models.CharField(max_length=50)),
                ('station_from', models.CharField(max_length=50)),
                ('station_to', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('pnr', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
