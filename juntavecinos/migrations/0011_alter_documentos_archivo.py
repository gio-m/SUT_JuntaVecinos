# Generated by Django 4.2.6 on 2023-11-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntavecinos', '0010_auto_20231124_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='archivo',
            field=models.FileField(upload_to='documentos/', verbose_name='Agrega algún documento o boleta que compruebe tu identidad'),
        ),
    ]
