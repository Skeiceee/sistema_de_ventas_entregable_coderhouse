from django.shortcuts import render
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

# Producto
def productos(request):
    context = { 'productos': Producto.objects.all().order_by("id")}
    return render(request, 'aplicacion/producto/productos.html', context)

def productoCreate(request):
    if request.method == "POST":
        myForm = ProductoForm(request.POST)

        if myForm.is_valid():
            nombre = myForm.cleaned_data.get("nombre")
            detalle = myForm.cleaned_data.get("detalle")
            producto = Producto(nombre=nombre, detalle=detalle)
            producto.save()

            context = {'productos' : Producto.objects.all().order_by("id")}
            return render(request, "aplicacion/producto/productos.html", context)

    else:
        myForm = ProductoForm()

    return render(request, "aplicacion/producto/productoForm.html", {"form": myForm})

def productoBuscar(request):
    return render(request, "aplicacion/producto/productoBuscar.html")

def productoEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        context = { 'productos': productos }
        return render(request, 'aplicacion/producto/productos.html', context)
    
    context = { 'productos': Producto.objects.all() }
    return render(request, 'aplicacion/producto/productos.html', context)

# Vendedor
def vendedores(request):
    context = { 'vendedores': Vendedor.objects.all().order_by("id") }
    return render(request, 'aplicacion/vendedor/vendedores.html', context)

def vendedorCreate(request):
    if request.method == "POST":
        myForm = VendedorForm(request.POST)

        if myForm.is_valid():
            nombre = myForm.cleaned_data.get("nombre")
            apellido = myForm.cleaned_data.get("apellido")
            email = myForm.cleaned_data.get("email")
            rubro = myForm.cleaned_data.get("rubro")

            vendedor = Vendedor(nombre=nombre, apellido=apellido, email=email, rubro=rubro)
            vendedor.save()
            
            context = {'vendedores' : Vendedor.objects.all().order_by("id")}
            return render(request, "aplicacion/vendedor/vendedores.html", context)
   
    else:
        myForm = VendedorForm()

    return render(request, "aplicacion/vendedor/vendedorForm.html", {"form": myForm})

def vendedorBuscar(request):
    return render(request, "aplicacion/vendedor/vendedorBuscar.html")

def vendedorEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        vendedores = Vendedor.objects.filter(nombre__icontains=patron)
        context = { 'vendedores': vendedores }
        return render(request, 'aplicacion/vendedor/vendedores.html', context)
    
    context = { 'vendedores': Vendedor.objects.all() }
    return render(request, 'aplicacion/vendedor/vendedores.html', context)

# Comprador
def compradores(request):
    context = { 'compradores': Comprador.objects.all().order_by("id") }
    return render(request, 'aplicacion/comprador/compradores.html', context)

def ventas(request):
    context = { 'ventas': Venta.objects.all().order_by("id") }
    return render(request, 'aplicacion/venta/ventas.html', context)

# Adicionales
def acerca(request):
    return render(request, 'aplicacion/acerca.html')