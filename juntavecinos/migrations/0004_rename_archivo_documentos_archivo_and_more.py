# Generated by Django 4.2.6 on 2023-10-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntavecinos', '0003_juntavecinos_tiposperfil_reuniones_notificaciones_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentos',
            old_name='Archivo',
            new_name='archivo',
        ),
        migrations.RenameField(
            model_name='documentos',
            old_name='DescripcionDocumento',
            new_name='descripcion_documento',
        ),
        migrations.RenameField(
            model_name='documentos',
            old_name='FechaPublicacion',
            new_name='fecha_publicacion',
        ),
        migrations.RenameField(
            model_name='documentos',
            old_name='NombreDocumento',
            new_name='nombre_documento',
        ),
        migrations.RenameField(
            model_name='documentos',
            old_name='TipoDocumento',
            new_name='tipo_documento',
        ),
        migrations.AlterField(
            model_name='documentos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Reuniones',
        ),
    ]