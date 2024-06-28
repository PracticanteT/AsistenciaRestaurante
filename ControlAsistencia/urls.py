from django.urls import path
from . import views 
from .views import crear_empleado

urlpatterns = [
    path('registro/', views.registro_asistencia, name='registro_asistencia'),
    path('exportar/', views.exportar_form, name='exportar_form'),
    path('exportar-excel/', views.exportar_registros_excel, name='exportar_registros_excel'),
    path('crear-empleado/', crear_empleado, name='crear_empleado'),
    
]
