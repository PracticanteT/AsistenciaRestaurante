# Generated by Django 5.0.6 on 2024-06-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAsistencia', '0004_alter_empleado_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='genero',
            field=models.CharField(choices=[('masculino', 'MASCULINO'), ('femenino', 'FEMENINO')], max_length=25),
        ),
    ]
