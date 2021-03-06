# Generated by Django 3.2.4 on 2021-07-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_way', '0002_alter_city_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=70, unique=True, verbose_name='City'),
        ),
    ]
