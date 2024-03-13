from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    detalle = forms.CharField(max_length=500,required=True)

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length = 40, required=True)
    apellido = forms.CharField(max_length = 40, required=True)
    email = forms.EmailField(required=True)
    rubro = forms.CharField(max_length = 40, required=True)

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
