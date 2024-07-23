# Generated by Django 4.2 on 2024-03-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0015_street_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(db_index=True, max_length=300)),
                ('sity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='src', to='location.locationavailable')),
                ('stret', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='src', to='location.street')),
            ],
        ),
    ]
