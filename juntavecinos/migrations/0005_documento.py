# Generated by Django 4.2.6 on 2023-10-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntavecinos', '0004_rename_archivo_documentos_archivo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=255)),
                ('tipo_documento', models.CharField(max_length=255)),
                ('fecha_publicacion', models.DateField()),
                ('descripcion_documento', models.TextField()),
                ('archivo', models.FileField(upload_to='documentos/')),
            ],
        ),
    ]
