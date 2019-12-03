"""barbershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('barber.urls'),name="inicio"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('registrarCliente/', include('barber.urls'), name="registrarCliente"),
    path('login/cliente/', include('barber.urls'), name="cliente"),
    path('logout/', LogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('login/admin/', include('barber.urls'), name="administrador"),
    path('actualizarCliente/<int:cliente_id>',
         include('barber.urls'), name="actualizarCliente"),
    path('borrarCliente/<int:cliente_id>',
         include('barber.urls'), name="ClienteBorrar"),
    path('listarCliente/', include('barber.urls'), name="listarCliente"),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                                           email_template_name="registration/password_reset_email.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('productoCliente/',include('barber.urls'),name="productoCliente"),
    path('categoriaProducto/',include('barber.urls'),name="categoriaProducto"),
    path('listarProductos/',include('barber.urls'),name="listarProductos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)