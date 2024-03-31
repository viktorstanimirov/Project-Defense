# Generated by Django 5.0.3 on 2024-03-31 13:41

import FastFoodApp.users.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='Username must be at least 3 chars long!'), FastFoodApp.users.validators.validate_username])),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]