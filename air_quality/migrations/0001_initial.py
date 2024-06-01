# Generated by Django 5.0.6 on 2024-06-01 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Temperature', 'Temperature'), ('Humidity', 'Humidity'), ('CO2', 'CO2'), ('PM2.5', 'PM2.5'), ('PM10', 'PM10')], max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('installation_date', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pm25', models.FloatField()),
                ('pm10', models.FloatField()),
                ('co2', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air_quality.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='air_quality.sensor')),
            ],
        ),
    ]