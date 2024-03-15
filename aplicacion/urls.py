from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home , name="home"),
    path('acerca/', acerca , name="acerca"),

    path('login/', login_request, name="login"),
    path('registrar/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),

    path('perfil/', editProfile, name="profile"),
    path('cambiar/contraseña/', editPassword, name="password_change"),
    path('agregar/avatar/', addAvatar, name="add_avatar"),

    path('productos/', ProductoList.as_view(), name="productos"),
    path('productos/agregar', ProductoCreate.as_view(), name="producto_create"),
    path('productos/editar/<int:pk>', ProductoUpdate.as_view(), name="producto_update"),
    path('productos/eliminar/<int:pk>', ProductoDelete.as_view(), name="producto_delete"),
    path('productos/encontrar', productoEncontrar , name="producto_encontrar"),

    path('vendedores/', VendedorList.as_view(), name="vendedores"),
    path('vendedores/agregar', VendedorCreate.as_view(), name="vendedor_create"),
    path('vendedores/editar/<int:pk>', VendedorUpdate.as_view(), name="vendedor_update"),
    path('vendedores/eliminar/<int:pk>', VendedorDelete.as_view(), name="vendedor_delete"),
    path('vendedores/encontrar', vendedorEncontrar , name="vendedor_encontrar"),

    path('compradores/', CompradorList.as_view(), name="compradores"),
    path('compradores/agregar', CompradorCreate.as_view(), name="comprador_create"),
    path('compradores/editar/<int:pk>', CompradorUpdate.as_view(), name="comprador_update"),
    path('compradores/eliminar/<int:pk>', CompradorDelete.as_view(), name="comprador_delete"),
    path('compradores/encontrar', compradorEncontrar , name="comprador_encontrar"),

    path('ventas/', VentaList.as_view(), name="ventas"),
    path('ventas/agregar', VentaCreate.as_view(), name="venta_create"),
    path('ventas/editar/<int:pk>', VentaUpdate.as_view(), name="venta_update"),
    path('ventas/eliminar/<int:pk>', VentaDelete.as_view(), name="venta_delete"),
    path('ventas/encontrar', ventaEncontrar , name="venta_encontrar"),

]
