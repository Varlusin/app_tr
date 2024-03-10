# Generated by Django 4.2 on 2024-02-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Typefutur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, unique=True)),
                ('names_en', models.CharField(max_length=50, null=True, unique=True)),
                ('names_ru', models.CharField(max_length=50, null=True, unique=True)),
                ('names_hy', models.CharField(max_length=50, null=True, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('publish', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Մեր մասին',
                'verbose_name_plural': 'Մեր մասին',
            },
        ),
        migrations.CreateModel(
            name='TypeFuturNavigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, unique=True)),
                ('names_en', models.CharField(max_length=50, null=True, unique=True)),
                ('names_ru', models.CharField(max_length=50, null=True, unique=True)),
                ('names_hy', models.CharField(max_length=50, null=True, unique=True)),
                ('discriptions', models.TextField()),
                ('discriptions_en', models.TextField(null=True)),
                ('discriptions_ru', models.TextField(null=True)),
                ('discriptions_hy', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='mayin_img')),
                ('publish', models.BooleanField()),
                ('caregory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat_fut', to='mayin.typefutur')),
            ],
            options={
                'verbose_name': 'Նորություն աշխատանք ...',
                'verbose_name_plural': 'Նորություններ աշխատանք ...',
            },
        ),
    ]
