import pandas as pd
from django.utils.timezone import now
import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsistenciaRestaurante.settings')
django.setup()

from ControlAsistencia.models import Empleado

def load_excel_data(file_path):
    # Leer el archivo Excel
    df = pd.read_excel(file_path)

    # Iterar a través de las filas del DataFrame e insertar los datos en la base de datos
    for index, row in df.iterrows():
        Empleado.objects.create(
            codigo=row['CODIGO'],
            nombre=row['NOMBRE'],
            cedula=row['NUMCEDULA'],
            fecha_registro=now().date(),
            hora_registro=now().time()
        )

if __name__ == "__main__":
    # Ruta del archivo Excel
    file_path = r'C:\Datos\datos.xlsx'
    load_excel_data(file_path)
    print("Datos cargados con éxito")