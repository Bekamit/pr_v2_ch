# Generated by Django 4.2.4 on 2023-08-14 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отель',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=500)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронировании',
            },
        ),
    ]