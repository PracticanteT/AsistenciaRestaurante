import pandas as pd
from django.utils.timezone import now
import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsistenciaRestaurante.settings')
django.setup()

from ControlAsistencia.models import Empleado

def load_excel_data(file_path):
    # Leer el archivo Excel tratando la columna de códigos como texto
    df = pd.read_excel(file_path, dtype={'CODIGO': str, 'NUMCEDULA': str})  # Especifica que la columna 'CODIGO' debe ser tratada como texto

    # Iterar a través de las filas del DataFrame e insertar los datos en la base de datos
    for index, row in df.iterrows():
        Empleado.objects.create(
            codigo=row['CODIGO'],  # Asegúrate de que el campo 'codigo' en el modelo Empleado es un CharField
            nombre=row['NOMBRE'],
            cedula=row['NUMCEDULA'],
            centro_de_costos=row['CENCOS'],
            cargo=row['NOMBRE_CARGO'],
            fecha_registro=now().date(),
            hora_registro=now().time()
        )

if __name__ == "__main__":
    # Ruta del archivo Excel
    file_path = r'C:\Datos\DATA_NUEVA.xlsx'
    load_excel_data(file_path)
    print("Datos cargados con éxito")
