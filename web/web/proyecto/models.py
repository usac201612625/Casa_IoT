"""
Crea tabla dentro de base de datos
"""
from django.db import models

class EjemploMedicion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    valor1 = models.FloatField(default=0)
    valor2 = models.FloatField(default=0)
    valor3 = models.FloatField(default=0)

    def __str__(self):
        return f'EjemploMedicion: {self.valor1},{self.valor2},{self.valor3}'