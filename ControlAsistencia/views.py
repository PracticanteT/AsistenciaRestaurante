from django.shortcuts import render
from .models import Empleado
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware
from django.http import HttpResponse
from openpyxl import Workbook
from django.utils.timezone import now
from django.utils import timezone




@csrf_exempt
def registro_asistencia(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo').strip()  # Asegurarse de quitar espacios innecesarios
        # Intenta obtener el empleado o crea un registro mínimo con solo el código
        empleado, created = Empleado.objects.get_or_create(
            codigo=codigo,
            defaults={
                'nombre': 'Nombre temporal',  # Evita dejarlo completamente vacío si es un campo requerido
                'cedula': 'Cédula temporal',  # Evita dejarlo completamente vacío si es un campo requerido
                'fecha_registro': now().date(),  # Fecha actual con zona horaria
                'hora_registro': now().time(),  # Hora actual con zona horaria, corregido
            }
        )
        # Información para el cliente sobre si el empleado fue creado o encontrado
        response_data = {
            'codigo': empleado.codigo,
            'nombre': empleado.nombre,
            'cedula': empleado.cedula,
            'fecha': empleado.fecha_registro.strftime('%Y-%m-%d'),
            'hora': empleado.hora_registro.strftime('%H:%M:%S'),
            'mensaje': 'Empleado creado exitosamente con el código proporcionado.' if created else 'Empleado encontrado con detalles existentes.'
        }
        return JsonResponse(response_data)

    return render(request, 'ControlAsistencia/registro_asistencia.html')

def exportar_registros_excel(request):
    fecha_inicio = request.GET.get('inicio')
    fecha_fin = request.GET.get('fin')

    if fecha_inicio and fecha_fin:
        fecha_inicio = make_aware(datetime.strptime(fecha_inicio, '%Y-%m-%d'))
        fecha_fin = make_aware(datetime.strptime(fecha_fin, '%Y-%m-%d'))

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="registros_asistencia.xlsx"'

        wb = Workbook()
        ws = wb.active
        ws.title = "Registros de Asistencia"
        ws.append(['Código', 'Nombre', 'Cédula', 'Fecha', 'Hora'])
        
        empleados = Empleado.objects.filter(fecha_registro__range=[fecha_inicio, fecha_fin])
        for empleado in empleados:
            ws.append([
                empleado.codigo,
                empleado.nombre,
                empleado.cedula,
                empleado.fecha_registro,
                empleado.hora_registro.strftime('%H:%M:%S')
            ])

        wb.save(response)
        return response
    else:
        return HttpResponse("Fechas no proporcionadas.")
    
def exportar_form(request):
        return render(request, 'ControlAsistencia/exportar_form.html')