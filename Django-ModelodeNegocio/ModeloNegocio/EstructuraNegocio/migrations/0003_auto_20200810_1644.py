# Generated by Django 3.0.5 on 2020-08-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EstructuraNegocio', '0002_auto_20200810_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='id',
            field=models.CharField(default=None, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='canal',
            name='id',
            field=models.CharField(default=None, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='participante',
            name='id',
            field=models.CharField(default=None, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='id',
            field=models.CharField(default=None, max_length=30, primary_key=True, serialize=False),
        ),
    ]
