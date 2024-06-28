from django.shortcuts import render, redirect
from .models import Empleado
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware, now
from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import EmpleadoForm


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='administradores').exists()


@login_required
@csrf_exempt
def registro_asistencia(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo').strip()
        hora_cliente = request.POST.get('hora_cliente').strip()
        try:
            empleado = Empleado.objects.get(codigo=codigo)
            empleado.fecha_registro = now().date()
            empleado.hora_registro = now().time()
            empleado.hora_marcacion_real = hora_cliente
            empleado.save()
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
                'hora': empleado.hora_marcacion_real,
            })
        return JsonResponse(response_data)

    return render(request, 'ControlAsistencia/registro_asistencia.html')

@user_passes_test(is_admin)
@login_required
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
        ws.append(['Código', 'Nombre', 'Cédula', 'Fecha', 'Hora de Marcación'])

        empleados = Empleado.objects.filter(fecha_registro__range=[fecha_inicio, fecha_fin])
        total_registros = empleados.count()
        
        for empleado in empleados:
            ws.append([
                empleado.codigo,
                empleado.nombre,
                empleado.cedula,
                empleado.fecha_registro.strftime('%Y-%m-%d'),
                empleado.hora_marcacion_real
            ])

        # Añadir la suma total de los registros
        ws.append([])
        ws.append(['Total de registros', total_registros])

        wb.save(response)
        return response
    else:
        return HttpResponse("Fechas no proporcionadas.")
    
    
@user_passes_test(is_admin)
@login_required   
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.hora_registro = now().time()  # Establece la hora de registro automáticamente
            empleado.hora_marcacion_real = now().strftime('%H:%M:%S')
            empleado.save()
            return redirect('registro_asistencia')  # Redirige a la vista de registro de asistencia después de crear el empleado
    else:
        form = EmpleadoForm()
    return render(request, 'ControlAsistencia/crear_empleado.html', {'form': form})

@user_passes_test(is_admin)
def exportar_form(request):
    return render(request, 'ControlAsistencia/exportar_form.html')

