# Generated by Django 4.2 on 2024-02-21 23:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_delete_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=70)),
                ('center_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('sity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildings', to='location.locationavailable')),
                ('stret', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buildings', to='location.street')),
            ],
        ),
    ]
