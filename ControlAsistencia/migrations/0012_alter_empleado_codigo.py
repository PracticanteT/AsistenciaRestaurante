# Generated by Django 5.0.6 on 2024-07-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAsistencia', '0011_asistencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
