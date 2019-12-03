from django.contrib import admin
from .models import Cliente , Fotos , Categoria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Fotos)
