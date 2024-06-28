
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    fecha_registro = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Empleado
        fields = ['codigo', 'nombre', 'cedula', 'fecha_registro']