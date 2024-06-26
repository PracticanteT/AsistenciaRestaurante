from django.shortcuts import render
from .models import Empleado
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware, now
from django.http import HttpResponse
from openpyxl import Workbook

@csrf_exempt
def registro_asistencia(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo').strip()
        try:
            empleado = Empleado.objects.get(codigo=codigo)  # Intenta obtener el empleado
            empleado.fecha_registro = now().date()
            empleado.hora_registro = now().time()
            empleado.save()  # Guarda los cambios en la base de datos
            mensaje = 'Registro del empleado actualizado con la hora actual.'
        except Empleado.DoesNotExist:
            mensaje = 'Error: Empleado no encontrado.'
            empleado = None

        response_data = {
            'codigo': codigo,
            'mensaje': mensaje
        }
        if empleado:
            response_data.update({
                'nombre': empleado.nombre,
                'cedula': empleado.cedula,
                'fecha': empleado.fecha_registro.strftime('%Y-%m-%d'),
                'hora': empleado.hora_registro.strftime('%H:%M:%S'),
            })
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