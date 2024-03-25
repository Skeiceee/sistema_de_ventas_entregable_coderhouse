from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Vendedor, Comprador, Producto, Venta, Avatar

class Producto(models.Model):
    nombre = models.CharField(max_length = 40)
    detalle = models.CharField(max_length = 500)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"

class Comprador(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()

    class Meta:
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    rubro = models.CharField(max_length = 40)

    class Meta:
        ordering = ["nombre", "apellido"]
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Venta(models.Model):
    nombreVendedor = models.CharField(verbose_name="Nombre del vendedor",max_length = 40)
    nombreComprador = models.CharField(verbose_name="Nombre del comprador", max_length = 40)
    nombreProducto = models.CharField(verbose_name="Nombre del Producto", max_length = 40, default='')
    entregado = models.BooleanField()

    class Meta:
        ordering = ["nombreVendedor", "nombreComprador"]

    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"