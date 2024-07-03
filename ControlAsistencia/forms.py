# Importa las herramientas necesarias para crear formularios en Django
from django import forms
# Importa el modelo Empleado desde el archivo models en el mismo directorio
from .models import Empleado

# Define una clase de formulario para el modelo Empleado, que hereda de forms.ModelForm
class EmpleadoForm(forms.ModelForm):
    # Agrega un campo personalizado para la fecha de registro utilizando un widget de entrada de fecha
    fecha_registro = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Clase interna que proporciona metadatos al formulario
    class Meta:
        # Especifica el modelo al que está vinculado este formulario
        model = Empleado
        # Lista los campos del modelo que se incluirán en el formulario
        fields = ['codigo', 'nombre', 'cedula', 'fecha_registro']
