# Generated by Django 3.1.1 on 2020-09-03 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
