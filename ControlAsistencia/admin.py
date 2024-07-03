# Importa las funcionalidades necesarias de Django
from django.contrib import admin  # Importa el módulo de administración de Django

# Importa el modelo Empleado desde el archivo models del mismo directorio que este archivo
from .models import Empleado

# Registra el modelo Empleado en el sitio de administración
# Esto permite que el modelo sea manejable a través de la interfaz de administración de Django
admin.site.register(Empleado)
