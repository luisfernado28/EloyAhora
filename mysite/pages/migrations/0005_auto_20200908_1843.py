# Generated by Django 3.1.1 on 2020-09-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200905_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
