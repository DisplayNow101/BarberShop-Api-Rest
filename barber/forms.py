from django import forms
from .models import Cliente , Fotos , Categoria


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['user', 'rut', 'correo', 'nombre', 'apellido', 'fechaNacimiento',
                  'telefonoContacto', 'tipoVivienda', 'Region', 'Ciudad']

class FotosForm(forms.ModelForm):
    
    class Meta:
        model = Fotos
        fields = ['categoria','titulo','foto','favorito','comentario']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre']
