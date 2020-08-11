# Generated by Django 3.0.5 on 2020-08-10 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioNegocio',
            fields=[
                ('id', models.BigIntegerField(default=None, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortafolioServicios.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigIntegerField(default=None, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortafolioServicios.ServicioNegocio')),
            ],
        ),
        migrations.CreateModel(
            name='ObjetoNegocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortafolioServicios.ServicioNegocio')),
            ],
        ),
    ]
