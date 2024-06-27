from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_asistencia, name='registro_asistencia'),
    path('exportar/', views.exportar_form, name='exportar_form'),
    path('exportar-excel/', views.exportar_registros_excel, name='exportar_registros_excel'),
]
