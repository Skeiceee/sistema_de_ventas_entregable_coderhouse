# Generated by Django 5.0.2 on 2024-03-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_venta_options_remove_venta_fechadecompra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='nombreProducto',
            field=models.CharField(default=' ', max_length=40, verbose_name='Nombre del Producto'),
        ),
    ]
