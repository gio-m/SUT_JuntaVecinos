# Generated by Django 4.2.6 on 2023-11-24 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('juntavecinos', '0008_alter_documentos_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
