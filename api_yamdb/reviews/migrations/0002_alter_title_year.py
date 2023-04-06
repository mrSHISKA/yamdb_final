# Generated by Django 3.2 on 2022-12-14 14:54


import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2022, message='год выпуска не может быть больше текущего')], verbose_name='Год выпуска'),
        ),
    ]
