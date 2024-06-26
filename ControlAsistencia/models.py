from django.db import models

class Empleado(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=25, choices=[
        ('masculino', 'MASCULINO'),
        ('femenino', 'FEMENINO')
        
    ])

    def __str__(self):
        return self.nombre
