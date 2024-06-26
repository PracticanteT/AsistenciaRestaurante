from django.urls import path
from .views import registro_asistencia

urlpatterns = [
    path('registro/', registro_asistencia, name='registro_asistencia'),
]
