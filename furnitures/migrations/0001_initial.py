# Generated by Django 5.0.4 on 2024-05-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furnitures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WhatWeDo', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
