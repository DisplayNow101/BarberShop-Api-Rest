from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from .models import Cliente, User
from .forms import ClienteForm
from . import views
import json
import unittest
# Create your tests here.

#Test del cliente , ya como extendimos el usuario user para agregar mas atributos y
#Asi sea mas facil el logeo de multiusuario (administrador,cliente) 
#Nuestro modelo Cliente recibe la foreignkey del user.
class TestCliente(TestCase):

    def create_user_del_cliente_para_login(self, username="eduardo", password="eduardo77"):
        return User.objects.create(username=username, password=password)

    def test_create_user_del_cliente_se_creo(self):
        cl = self.create_user_del_cliente_para_login()
        self.assertTrue(isinstance(cl, User))

    def update_user_del_cliente(self, id=5,username="marcelo"):
        return User.objects.update(id=id,username=username)

    def test_update_user_del_cliente(self):
        cl = self.update_user_del_cliente()
        self.assertFalse(isinstance(cl, User))

    def test_valid_form_sin_password(self):
        cl = User.objects.create(
            username="eduardo", email="e.poncer@alumnos.duoc.cl")
        data = {'username': cl.username, 'email': cl.email}
        form = ClienteForm(data=data)
        self.assertFalse(form.is_valid())
        print(data)

    def test_valid_form_con_password(self):
        cl = User.objects.create(
            username="Duoc", email="eduardo@gmail.com", password="marcelo77")
        data = {'username': cl.username,
                'email': cl.email, 'password': cl.password}
        form = ClienteForm(data=data)
        self.assertFalse(form.is_valid())
        print(data)

#Test para corroborar el funcionamiento de los caracteres
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_strings_iguales(self): 
        self.assertEqual( 'eduardo', 'eduardo') 
  
    def test_upper(self):         
        self.assertEqual('eduardo'.upper(), 'EDUARDO') 
  
    def test_isupper(self):         
        self.assertTrue('MARCELO'.isupper()) 
        self.assertFalse('Marcelo'.isupper()) 
   
    def test_strip(self):         
        s = ' barberforshop '
        print(s.strip(' '))
  
    def test_split(self):         
        s = 'Bienvenido A BarberShop'
        self.assertEqual(s.split(), ['Bienvenido','A','BarberShop']) 
        with self.assertRaises(TypeError): 
            s.split(2) 