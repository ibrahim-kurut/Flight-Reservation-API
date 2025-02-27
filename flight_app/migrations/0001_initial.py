# Generated by Django 5.0.7 on 2024-07-15 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=100)),
                ('operation_airlines', models.CharField(max_length=100)),
                ('departure_city', models.CharField(max_length=100)),
                ('arrival_city', models.CharField(max_length=100)),
                ('date_of_departure', models.DateField()),
                ('estimated_time_of_departure', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('passenger_type', models.CharField(choices=[('Adult', 'Adult'), ('Child', 'Child'), ('Infant', 'Infant')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_app.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_app.passenger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
