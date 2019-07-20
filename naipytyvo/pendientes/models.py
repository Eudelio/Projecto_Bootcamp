from django.db import models

# Create your models here.

class Info(models.Model):
    nombre = models.TextField(max_length=20)
    telefono = models.IntegerField(max_length=20)
    ciudad = models.TextField(max_length=20)
    servicio = models.TextField(max_length=20)
    breve_descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre