from django.db import models

class Empleado(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    hora_registro = models.TimeField()

    def __str__(self):
        return self.nombre
