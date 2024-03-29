# Generated by Django 2.2.6 on 2019-10-21 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, null=True)),
                ('correo', models.EmailField(max_length=254, null=True, unique=True)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellido', models.CharField(max_length=40, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('telefonoContacto', models.CharField(max_length=12, null=True, unique=True)),
                ('tipoVivienda', models.CharField(choices=[('Casa con patio grande', 'Casa con patio grande'), ('Casa con patio pequeño', 'Casa con patio pequeño'), ('Casa sin patio', 'Casa sin patio'), ('Departamento', 'Departamento')], max_length=40, null=True)),
                ('Region', models.CharField(choices=[('Metropolitana', 'Metropolitana'), ('Valparaíso', 'Valparaíso'), ('Coquimbo', 'Coquimbo')], max_length=40, null=True)),
                ('Ciudad', models.CharField(choices=[('Santiago', 'Santiago'), ('Melipilla', 'Melipilla'), ('Peñaflor', 'Peñaflor'), ('Buin', 'Buin')], max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
