# Generated by Django 3.1.1 on 2020-09-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('typeofuser', models.IntegerField(choices=[(1, 'Vendedor'), (2, 'Comprador')])),
                ('cellphone', models.CharField(max_length=15)),
                ('direction', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofproduct', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('dimentions', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('owner', models.ManyToManyField(to='api_basic.user')),
                ('tags', models.ManyToManyField(to='api_basic.Tag')),
            ],
        ),
    ]
