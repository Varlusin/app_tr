# Generated by Django 4.2 on 2024-02-20 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_street'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Street',
        ),
    ]
