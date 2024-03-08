from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    detalle = forms.CharField(max_length=500,required=True)

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length = 40, required=True)
    apellido = forms.CharField(max_length = 40, required=True)
    email = forms.EmailField(required=True)
    rubro = forms.CharField(max_length = 40, required=True)