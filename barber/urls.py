from django.urls import path, include
from . import views
from .views import ClienteViewSet
#Import Routers
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('login/', views.login, name="login"),
    path('registrarCliente/', views.ClienteCreate.as_view(),
         name="registrarCliente"),
    path('login/cliente/', views.cliente, name="cliente"),
    path('login/admin/', views.admin, name="administrador"),
    path('actualizarCliente/<int:cliente_id>',
         views.ClienteActualizar, name="actualizarCliente"),
    path('borrarCliente/<int:cliente_id>',
         views.ClienteBorrar, name="borrarCliente"),
    path('listarCliente/', views.ClienteList.as_view(), name="listarCliente"),
    path('productoCliente/', views.FotosView, name="productoCliente"),
    path('categoriaProducto/', views.CategoriaView.as_view(),
         name="categoriaProducto"),
    path('listarProductos/',views.ProductoList.as_view(),name="listarProductos"),
    #Ruta para la Api
    path('api/', include(router.urls)),
    
]
