# Generated by Django 3.1.1 on 2020-09-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0007_auto_20200912_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ManyToManyField(to='api_basic.User'),
        ),
    ]
