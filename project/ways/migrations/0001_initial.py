# Generated by Django 3.2.4 on 2021-07-22 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('find_way', '0003_auto_20210716_1920'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Way number')),
                ('travel_time', models.PositiveIntegerField(verbose_name='Travel time')),
                ('finish_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='way_finish_city_set', to='find_way.city', verbose_name='Finish')),
                ('start_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='way_start_city_set', to='find_way.city', verbose_name='Start')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Trains List')),
            ],
            options={
                'verbose_name': 'Way',
                'verbose_name_plural': 'Ways',
                'ordering': ['travel_time'],
            },
        ),
    ]
