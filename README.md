# BarberShop
Proyecto Encargo N°2

Login Administrador:
usuario= eduardo 
contraseña= eduardo

Login Cliente:
usuario= marcelo
contraseña= eduardo77

En la parte del administrador al registrar al usuario en la parte de añadir user ahi es donde pertenece el login para los usuarios cuando se crea el user se puede utilizar de id en la pagina de registro de usuario ahi lo ocupamos para llenar con los demas atributos del cliente , en el Listar colocamos la funcion de eliminar y modificar como reciben una id es mas facil de esta manera que escribiendo en la url , asi lo hace automaticamente.

Colocamos un "agregar producto" junto con un titulo nombre descripcion y subir una imagen esa parte lo hace el administrador, en la cual despues vera en la parte de cliente el registro de estos productos, en el html5 del logeo del cliente antes del footer podra ver una imagen junto con un hipervinculo que lo lleva los productos que estan disponibles en BarberShop, como anteriormente estos productos lo subira el administrador para que los visualice el cliente.

Aplicamos un logout para los 2 usuarios , los devuelve al login.

#Test del cliente , ya como extendimos el usuario user para agregar mas atributos y
#Asi sea mas facil el logeo de multiusuario (administrador,cliente) 
#Nuestro modelo Cliente recibe la foreignkey del user.

Testeamos el cliente con TestCase

Creamos 2 funciones una que crea el objecto de user y el otro que recibe la instancia comparando el usuario User del sistema con el usuario recien creado.

Creamos otra funcion para el update , el mismo procedimiento solo cambie que recibe como parametro de entrada la id para identificar que usuario quiere modificar.

Probamos el test con los formularios si reciben la validacion correspondientes creados en el forms.py 

Mas abajo creamos unos testeo utilizando unittest para los strings del sistema

*Comparando si son iguales
*Si escriben en mayusculas o minusculas
*Por separado


Creamos un archivo llamado "serializers.py", donde hicimos un serializador de Cliente. Ahi importamos el rest_framework y la clase Cliente

En "views.py" creamos una clase llamada "ClienteViewSet", que nos permite crear la consulta a la BD en JSON

En urls.py hicimos un import routers para poder definir la ruta a la api
