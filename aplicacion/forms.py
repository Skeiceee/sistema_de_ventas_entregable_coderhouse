from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellidos/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)