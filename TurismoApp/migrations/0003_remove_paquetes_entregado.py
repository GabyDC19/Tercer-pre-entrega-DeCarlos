# Generated by Django 4.2.5 on 2023-10-22 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TurismoApp', '0002_rename_fecha_de_entrega_inicio_fechadesalida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquetes',
            name='entregado',
        ),
    ]
