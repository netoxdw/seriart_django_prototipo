# productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    tag_description = models.CharField(max_length=200, verbose_name="Descripción Corta", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(verbose_name="Stock", blank=True, null=True)

    def __str__(self):
        return self.nombre
    
