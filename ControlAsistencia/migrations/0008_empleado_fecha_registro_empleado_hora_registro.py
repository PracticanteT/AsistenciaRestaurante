# Generated by Django 5.0.6 on 2024-06-26 14:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAsistencia', '0007_alter_empleado_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fecha_registro',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='hora_registro',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
