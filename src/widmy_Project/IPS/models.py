#Este codigo no se utiliza. Pero lo voy a dejar quito por si acaso

from django.db import models

class IPS(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    
    def __str__(self) -> str:
        return '%s, %s' % (self.nombre, self.ciudad)