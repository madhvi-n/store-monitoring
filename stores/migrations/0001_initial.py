# Generated by Django 3.0.5 on 2023-02-22 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('timezone_str', models.CharField(default='America/Chicago', max_length=100)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='StoreStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_utc', models.DateTimeField()),
                ('status', models.CharField(max_length=8)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField()),
                ('start_time_local', models.TimeField()),
                ('end_time_local', models.TimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_hour', to='stores.Store')),
            ],
        ),
    ]