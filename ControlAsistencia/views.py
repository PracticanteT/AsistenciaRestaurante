from django.shortcuts import render
from .models import Empleado
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Temporalmente deshabilitar la protección CSRF para pruebas
def registro_asistencia(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        try:
            empleado = Empleado.objects.get(codigo=codigo)
            return JsonResponse({
                'nombre': empleado.nombre,
                'genero': empleado.genero,
                'fecha': datetime.datetime.now().strftime('%Y-%m-%d'),
                'hora': datetime.datetime.now().strftime('%H:%M:%S')
            })
        except Empleado.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
    else:
        return render(request, 'ControlAsistencia/registro_asistencia.html')