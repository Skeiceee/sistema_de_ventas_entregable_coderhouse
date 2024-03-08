from django.db import models

# Create your models here.
# Vendedor, Comprador, Producto, Venta

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
    nombreVendedor = models.CharField(max_length = 40)
    nombreComprador = models.CharField(max_length = 40)
    fechaDeCompra = models.DateField()
    entregado = models.BooleanField()

    class Meta:
        ordering = ["nombreVendedor", "nombreComprador", "fechaDeCompra"]

    def __str__(self):
        return f"{self.nombre}"