# Importa la función path de django.urls, que se utiliza para definir rutas dentro de la aplicación
from django.urls import path
# Importa todas las vistas del módulo actual
from . import views
# Importa específicamente la función crear_empleado desde el módulo views
from .views import crear_empleado

# Lista de patrones de URL para la aplicación
urlpatterns = [
    # Asigna la vista registro_asistencia a la URL 'registro/', y le da un nombre para poder referenciarlo en otros lugares como 'registro_asistencia'
    path('registro/', views.registro_asistencia, name='registro_asistencia'),

    # Asigna la vista exportar_form a la URL 'exportar/', y le da un nombre para poder referenciarlo en otros lugares como 'exportar_form'
    path('exportar/', views.exportar_form, name='exportar_form'),

    # Asigna la vista exportar_registros_excel a la URL 'exportar-excel/', y le da un nombre para poder referenciarlo en otros lugares como 'exportar_registros_excel'
    path('exportar-excel/', views.exportar_registros_excel, name='exportar_registros_excel'),

    # Asigna la función crear_empleado a la URL 'crear-empleado/', y le da un nombre para poder referenciarlo en otros lugares como 'crear_empleado'
    path('crear-empleado/', crear_empleado, name='crear_empleado'),

    path('eliminar_empleado/', views.eliminar_empleado, name='eliminar_empleado'),

    
]
