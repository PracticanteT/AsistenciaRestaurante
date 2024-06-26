from django.urls import path
from .views import registro_asistencia, exportar_registros_excel, exportar_form

urlpatterns = [
    path('registro/', registro_asistencia, name='registro_asistencia'),
    path('exportar/', exportar_form, name='exportar_form'),
    path('exportar-excel/', exportar_registros_excel, name='exportar_excel'),
]
