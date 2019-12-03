from django.shortcuts import render, redirect , render_to_response
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Fotos, Categoria
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ClienteForm, FotosForm, CategoriaForm
from django.core import serializers
from django.http.response import HttpResponseRedirect

#rest_framework
from rest_framework import viewsets
from .serializers import ClienteSerializer



# Create your views here.


def login_User(request):
    return render(request, 'registration/login.html', {})


def inicio(request):
    return render(request, 'registration/inicio.html', {})


def cliente(request):
    return render(request, 'registration/cliente.html', {})


def admin(request):
    return render(request, 'registration/admin.html', {})


def borrarCliente(request):
    return render(request, 'barber/borrar.html', {})


def registrarCliente(request):
    return render(request, 'barber/registrarCliente.html', {})


def listarCliente(request):
    return render(request, 'barber/listarCliente.html', {})


def actualizarCliente(request):
    return render(request, 'barber/actualizar.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_superuser and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect("admin")
        elif user is not None and user.is_active and user is not user.is_superuser:
            auth.login(request, user)

            return HttpResponseRedirect("cliente")
        else:
            messages.info(request, "Credenciales incorrectas")
            return HttpResponseRedirect("/login")

    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)

    return HttpResponseRedirect("registration/login.html")

# Funciona Generics


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'barber/registrarCliente.html'
    success_url = reverse_lazy('registrarCliente')

#Hacemos una condicion para guardar el archivo
#y se carge la pagina productoCliente nuevamente
def FotosView(request):
    if request.method == 'POST':
        form = FotosForm(request.POST, request.FILES)
        if form.is_valid():
            # archivo se guarda
            form.save()
            return redirect('productoCliente')
    else:
        form = FotosForm()
    return render(request, 'barber/productoCliente.html', {'form': form})

#Creamos el generic de create view para la categoria
class CategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'barber/categoriaProducto.html'
    success_url = reverse_lazy('categoriaProducto')

# Funciona Generics Cliente
class ClienteList(ListView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'barber/listarCliente.html'

# Generic Producto
class ProductoList(ListView):
    model = Fotos
    form_class = FotosForm
    template_name = 'barber/listarProductos.html'

# Funcion Update
# Esta funcion la colocamos junto con el listar
def ClienteActualizar(request, cliente_id):
    # Recuperamos el registro de la base de datos por el id
    instancia = Cliente.objects.get(id=cliente_id)
    # creamos un formulario con los datos del objeto
    form = ClienteForm(instance=instancia)
    # Compronbamos si se envió el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos del objeto
        form = ClienteForm(request.POST, instance=instancia)
        # Si el formulario es valido....
        if form.is_valid():
            # Guardamos el formulario pero sin confirmar aun
            instancia = form.save(commit=False)
            # grabamos!!!
            instancia.save()
            # volvemos al listado :D
            return redirect('listarCliente')
    return render(request, "barber/actualizarCliente.html", {'form': form})

# Funcion Delete
# colocamos esta funcion en el listar
def ClienteBorrar(request, cliente_id):
    instancia = Cliente.objects.get(id=cliente_id)
    instancia.delete()
    return redirect('listarCliente')

#Clase ViewSet
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer