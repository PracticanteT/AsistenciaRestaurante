# Generated by Django 5.0.6 on 2024-06-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAsistencia', '0009_remove_empleado_genero_empleado_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hora_marcacion_real',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
