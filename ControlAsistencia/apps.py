# Importa AppConfig de django.apps, necesario para la configuración de aplicaciones en Django
from django.apps import AppConfig

# Define una clase de configuración para una aplicación específica de Django llamada 'ControlAsistencia'
class ControlasistenciaConfig(AppConfig):
    # Especifica el tipo de campo automático por defecto para los IDs en los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    # Establece el nombre de la aplicación que esta configuración representa
    name = 'ControlAsistencia'
