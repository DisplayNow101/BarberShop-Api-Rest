from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

Vivienda_Tipos = (
    ('Casa con patio grande', 'Casa con patio grande'),
    ('Casa con patio pequeño', 'Casa con patio pequeño'),
    ('Casa sin patio', 'Casa sin patio'),
    ('Departamento', 'Departamento'),
)

Regiones = (
    ('Metropolitana', 'Metropolitana'),
    ('Valparaíso', 'Valparaíso'),
    ('Coquimbo', 'Coquimbo'),
)

Ciudades = (
    ('Santiago', 'Santiago'),
    ('Melipilla', 'Melipilla'),
    ('Peñaflor', 'Peñaflor'),
    ('Buin', 'Buin'),
)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12,null=True)
    correo = models.EmailField(unique=True,null=True)
    nombre = models.CharField(max_length=40,null=True)
    apellido = models.CharField(max_length=40,null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
    telefonoContacto = models.CharField(unique=True, max_length=12, null=True)
    tipoVivienda = models.CharField(
        max_length=40, blank=False, null=True, choices=Vivienda_Tipos)
    Region = models.CharField(
        max_length=40, blank=False, null=True, choices=Regiones)
    Ciudad = models.CharField(
        max_length=40, blank=False, null=True, choices=Ciudades)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'correo'

    def get_short_name(self):
        return self.nombre

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Fotos(models.Model):

    categoria = models.ForeignKey(Categoria, null=True, blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, default='No title')
    foto = models.ImageField(upload_to='photos/')
    pub_fecha = models.DateField(auto_now_add=True)
    favorito = models.BooleanField(default=False)
    comentario = models.CharField(max_length=200, blank=True)

    def __titulo__(self):
        return self.titulo

