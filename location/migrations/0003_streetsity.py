# Generated by Django 4.2 on 2024-02-19 23:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_delete_streetsity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreetSity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('name_hy', models.CharField(max_length=200, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('sity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='street', to='location.locationavailable')),
            ],
        ),
    ]
