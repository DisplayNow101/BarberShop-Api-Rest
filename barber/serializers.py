#en este archivo se mantienen los serializadores
#sirven para cambiar datos 
#Ej. de "tipo_datos"--> JSON............. o visebersa

from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['user', 'rut', 'correo', 'nombre', 'apellido', 'fechaNacimiento',
                  'telefonoContacto', 'tipoVivienda', 'Region', 'Ciudad']

