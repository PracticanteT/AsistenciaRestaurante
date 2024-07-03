# Importa el módulo models de Django, que proporciona las bases para definir modelos de datos
from django.db import models

# Define el modelo Empleado que hereda de models.Model
class Empleado(models.Model):
    # Define varios campos para el modelo, incluyendo características como la longitud máxima y si son únicos
    codigo = models.CharField(max_length=100, unique=True)  # Campo para el código del empleado, debe ser único
    nombre = models.CharField(max_length=100)  # Campo para el nombre del empleado
    cedula = models.CharField(max_length=50)  # Campo para la cédula del empleado
    fecha_registro = models.DateField()  # Campo para la fecha de registro del empleado
    hora_registro = models.TimeField()  # Campo para la hora de registro del empleado
    hora_marcacion_real = models.CharField(max_length=8, null=True, blank=True)  # Campo opcional para la hora real de marcación

    # Método especial que define cómo se representa un objeto de este modelo como una cadena de texto
    def __str__(self):
        return self.nombre  # Retorna el nombre del empleado

# Define el modelo Asistencia que también hereda de models.Model
class Asistencia(models.Model):
    # Define un campo que es una clave foránea, relacionando cada Asistencia con un Empleado
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  # Si se elimina un Empleado, también se eliminan sus Asistencias
    fecha_registro = models.DateField()  # Campo para la fecha de registro de la asistencia
    hora_marcacion_real = models.CharField(max_length=8)  # Campo para la hora real de marcación

    # Método especial que define cómo se representa un objeto de este modelo como una cadena de texto
    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha_registro}"  # Formato personalizado que muestra el nombre del empleado y la fecha de registro
