# Generated by Django 3.2.4 on 2021-07-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('find_way', '0003_auto_20210716_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Train number')),
                ('travel_time', models.PositiveIntegerField(verbose_name='Travel time')),
                ('finish_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finish_city_set', to='find_way.city', verbose_name='Finish')),
                ('start_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_city_set', to='find_way.city', verbose_name='Start')),
            ],
            options={
                'verbose_name': 'Train',
                'verbose_name_plural': 'Trains',
                'ordering': ['travel_time'],
            },
        ),
    ]
