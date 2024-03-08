from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home , name="home"),
    
    path('productos/', productos , name="productos"),
    path('vendedores/', vendedores , name="vendedores"),
    path('compradores/', compradores , name="compradores"),
    path('ventas/', ventas , name="ventas"),
 
    path('acerca/', acerca , name="acerca"),

    path('productos/agregar', productosForm , name="producto_form"),
    path('vendedores/agregar', vendedorForm , name="vendedor_form"),

    path('productos/buscar', productoBuscar , name="producto_buscar"),
    path('productos/encontrar', productoEncontrar , name="producto_encontrar"),

    path('vendedores/buscar', vendedorBuscar , name="vendedor_buscar"),
    path('vendedores/encontrar', vendedorEncontrar , name="vendedor_encontrar"),
]
