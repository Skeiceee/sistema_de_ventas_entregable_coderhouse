from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

# Producto
@login_required
def productos(request):
    context = { 'productos': Producto.objects.all().order_by("id")}
    return render(request, 'aplicacion/producto/productos.html', context)

@login_required
def productoCreate(request):
    if request.method == "POST":
        myForm = ProductoForm(request.POST)

        if myForm.is_valid():
            nombre = myForm.cleaned_data.get("nombre")
            detalle = myForm.cleaned_data.get("detalle")
            producto = Producto(nombre=nombre, detalle=detalle)
            producto.save()

            return redirect(reverse_lazy('productos'))

    else:
        myForm = ProductoForm()

    return render(request, "aplicacion/producto/productoForm.html", {"form": myForm})
@login_required
def productoUpdate(request, id_producto):
    producto = Producto.objects.get(id=id_producto)

    if request.method == "POST":
        myForm = ProductoForm(request.POST)

        if myForm.is_valid():
            producto.nombre = myForm.cleaned_data.get("nombre")
            producto.detalle = myForm.cleaned_data.get("detalle")
            producto.save()

            return redirect(reverse_lazy('productos'))
    else:
        myForm = ProductoForm(initial={'nombre':producto.nombre, 'detalle':producto.detalle})

    return render(request, "aplicacion/producto/productoForm.html", {"form": myForm})
@login_required
def productoDelete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()

    return redirect(reverse_lazy('productos'))
@login_required
def productoBuscar(request):
    return render(request, "aplicacion/producto/productoBuscar.html")
@login_required
def productoEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        context = { 'productos': productos }
        return render(request, 'aplicacion/producto/productos.html', context)
    
    context = { 'productos': Producto.objects.all() }
    return render(request, 'aplicacion/producto/productos.html', context)

# Vendedor
@login_required
def vendedores(request):
    context = { 'vendedores': Vendedor.objects.all().order_by("id") }
    return render(request, 'aplicacion/vendedor/vendedores.html', context)

@login_required
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
            
            return redirect(reverse_lazy('vendedores'))
   
    else:
        myForm = VendedorForm()

    return render(request, "aplicacion/vendedor/vendedorForm.html", {"form": myForm})

@login_required
def vendedorUpdate(request, id_vendedor):
    vendedor = Vendedor.objects.get(id=id_vendedor)

    if request.method == "POST":
        myForm = VendedorForm(request.POST)

        if myForm.is_valid():
            vendedor.nombre = myForm.cleaned_data.get("nombre")
            vendedor.apellido = myForm.cleaned_data.get("apellido")
            vendedor.email = myForm.cleaned_data.get("email")
            vendedor.rubro = myForm.cleaned_data.get("rubro")
            vendedor.save()

            return redirect(reverse_lazy('vendedores'))

    else:
        myForm = VendedorForm(initial={'nombre':vendedor.nombre, 'apellido':vendedor.apellido, 'email':vendedor.email, 'rubro':vendedor.rubro})

    return render(request, "aplicacion/vendedor/vendedorForm.html", {"form": myForm})

@login_required
def vendedorDelete(request, id_vendedor):
    vendedor = Vendedor.objects.get(id=id_vendedor)
    vendedor.delete()

    return redirect(reverse_lazy('vendedores'))

@login_required
def vendedorBuscar(request):
    return render(request, "aplicacion/vendedor/vendedorBuscar.html")

@login_required
def vendedorEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        vendedores = Vendedor.objects.filter(nombre__icontains=patron)
        context = { 'vendedores': vendedores }
        return render(request, 'aplicacion/vendedor/vendedores.html', context)
    
    context = { 'vendedores': Vendedor.objects.all() }
    return render(request, 'aplicacion/vendedor/vendedores.html', context)

# Comprador
class CompradorList(LoginRequiredMixin, ListView):
    model = Comprador
    template_name = 'aplicacion/comprador/comprador_list.html'

class CompradorCreate(LoginRequiredMixin, CreateView):
    model = Comprador
    template_name = 'aplicacion/comprador/comprador_form.html'
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy('compradores')

class CompradorUpdate(LoginRequiredMixin, UpdateView):
    model = Comprador
    template_name = 'aplicacion/comprador/comprador_form.html'
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy('compradores')

class CompradorDelete(LoginRequiredMixin, DeleteView):
    model = Comprador
    template_name = 'aplicacion/comprador/comprador_confirm_delete.html'
    success_url = reverse_lazy('compradores')

# Venta
@login_required
def ventas(request):
    context = { 'ventas': Venta.objects.all().order_by("id") }
    return render(request, 'aplicacion/venta/ventas.html', context)

# Adicionales
def acerca(request):
    return render(request, 'aplicacion/acerca.html')


#Auth

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        myForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": myForm})

def register(request):
    if request.method == "POST":
        myForm = RegisterForm(request.POST)

        if myForm.is_valid():
            user = myForm.cleaned_data.get('username')
            myForm.save()
        else:
            return redirect(reverse_lazy('home'))
    else:
        myForm = RegisterForm()

    return render(request, "aplicacion/register.html", {"form": myForm})