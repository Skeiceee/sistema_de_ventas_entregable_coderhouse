from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home , name="home"),

    path('login/', login_request, name="login"),
    path('registrar/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),

    path('ventas/', ventas , name="ventas"),
 
    path('acerca/', acerca , name="acerca"),

    path('productos/', productos , name="productos"),
    path('productos/agregar', productoCreate , name="producto_create"),
    path('productos/editar/<id_producto>/', productoUpdate , name="producto_update"),
    path('productos/eliminar/<id_producto>/', productoDelete , name="producto_delete"),
    path('productos/buscar', productoBuscar , name="producto_buscar"),
    path('productos/encontrar', productoEncontrar , name="producto_encontrar"),

    path('vendedores/', vendedores , name="vendedores"),
    path('vendedores/agregar', vendedorCreate , name="vendedor_create"),
    path('vendedores/editar/<id_vendedor>/', vendedorUpdate , name="vendedor_update"),
    path('vendedores/eliminar/<id_vendedor>/', vendedorDelete , name="vendedor_delete"),
    path('vendedores/buscar', vendedorBuscar , name="vendedor_buscar"),
    path('vendedores/encontrar', vendedorEncontrar , name="vendedor_encontrar"),

    path('compradores/', CompradorList.as_view(), name="compradores"),
    path('compradores/agregar', CompradorCreate.as_view(), name="comprador_create"),
    path('compradores/editar/<int:pk>', CompradorUpdate.as_view(), name="comprador_update"),
    path('compradores/eliminar/<int:pk>', CompradorDelete.as_view(), name="comprador_delete"),

]
