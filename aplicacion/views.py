from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *

from django.contrib.auth import login, authenticate, update_session_auth_hash

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

# Producto
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'aplicacion/producto/producto_list.html'

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'aplicacion/producto/producto_form.html'
    fields = ["nombre", "detalle"]
    success_url = reverse_lazy('productos')

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'aplicacion/producto/producto_form.html'
    fields = ["nombre", "detalle"]
    success_url = reverse_lazy('productos')

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'aplicacion/producto/producto_confirm_delete.html'
    success_url = reverse_lazy('productos')

@login_required
def productoEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        context = { 'producto_list': productos }
        return render(request, 'aplicacion/producto/producto_list.html', context)
    
    context = { 'producto_list': Producto.objects.all() }
    return render(request, 'aplicacion/producto/producto_list.html', context)

# Vendedor
class VendedorList(LoginRequiredMixin, ListView):
    model = Vendedor
    template_name = 'aplicacion/vendedor/vendedor_list.html'

class VendedorCreate(LoginRequiredMixin, CreateView):
    model = Vendedor
    template_name = 'aplicacion/vendedor/vendedor_form.html'
    fields = ["nombre", "apellido", "email", "rubro"]
    success_url = reverse_lazy('vendedores')

class VendedorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    template_name = 'aplicacion/vendedor/vendedor_form.html'
    fields = ["nombre", "apellido", "email", "rubro"]
    success_url = reverse_lazy('vendedores')

class VendedorDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    template_name = 'aplicacion/vendedor/vendedor_confirm_delete.html'
    success_url = reverse_lazy('vendedores')

@login_required
def vendedorEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        vendedores = Vendedor.objects.filter(nombre__icontains=patron)
        context = { 'vendedor_list': vendedores }
        return render(request, 'aplicacion/vendedor/vendedor_list.html', context)
    
    context = { 'vendedor_list': Vendedor.objects.all() }
    return render(request, 'aplicacion/vendedor/vendedor_list.html', context)

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

def compradorEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        compradores = Comprador.objects.filter(nombre__icontains=patron)
        context = { 'comprador_list': compradores }
        return render(request, 'aplicacion/comprador/comprador_list.html', context)
    
    context = { 'comprador_list': Comprador.objects.all() }
    return render(request, 'aplicacion/comprador/comprador_list.html', context)


# Venta
class VentaList(LoginRequiredMixin, ListView):
    model = Venta
    template_name = 'aplicacion/venta/venta_list.html'

class VentaCreate(LoginRequiredMixin, CreateView):
    model = Venta
    template_name = 'aplicacion/venta/venta_form.html'
    fields = ["nombreVendedor", "nombreComprador", "fechaDeCompra", "entregado"]
    success_url = reverse_lazy('vendedores')

class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Venta
    template_name = 'aplicacion/venta/venta_form.html'
    fields = ["nombreVendedor", "nombreComprador", "fechaDeCompra", "entregado"]
    success_url = reverse_lazy('vendedores')

class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Venta
    template_name = 'aplicacion/venta/venta_confirm_delete.html'
    success_url = reverse_lazy('ventas')

def ventaEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        ventas = Venta.objects.filter(nombre__icontains=patron)
        context = { 'venta_list': ventas }
        return render(request, 'aplicacion/venta/venta_list.html', context)
    
    context = { 'venta_list': Venta.objects.all() }
    return render(request, 'aplicacion/venta/venta_list.html', context)

#Auth
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.svg"
            finally:
                request.session["avatar"] = avatar

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

# Edicion de perfil
@login_required
def editProfile(request):

    user = request.user

    if request.method == "POST":
        myForm = ProfileForm(request.POST)

        if myForm.is_valid():

            _user = User.objects.get(username=user)

            email = myForm.cleaned_data.get('email')
            first_name = myForm.cleaned_data.get('first_name')
            last_name = myForm.cleaned_data.get('last_name')

            _user.email = email
            _user.first_name = first_name
            _user.last_name = last_name

            _user.save()

            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('home'))
    else:
        myForm = ProfileForm(instance=user)

    return render(request, "aplicacion/profile.html", {"form": myForm})

@login_required
def editPassword(request):

    user = request.user

    if request.method == "POST":
        myForm = PasswordChangeForm(user, data=request.POST or None)

        if myForm.is_valid():
            myForm.save()
            update_session_auth_hash(request, myForm.user)
            return render(request, 'aplicacion/password_change_success.html', {'form': myForm})
        else:

            for field in myForm:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")

            return render(request, 'aplicacion/password_change.html', {'form': myForm})
    else:
        myForm = PasswordChangeForm(user)

    return render(request, "aplicacion/password_change.html", {"form": myForm})

@login_required
def addAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
                    
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/add_avatar.html", {"form": miForm} )

# Adicionales
def acerca(request):
    return render(request, 'aplicacion/acerca.html')