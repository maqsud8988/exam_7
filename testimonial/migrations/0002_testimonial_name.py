# Generated by Django 5.0.4 on 2024-05-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default='gegwe', max_length=100),
            preserve_default=False,
        ),
    ]