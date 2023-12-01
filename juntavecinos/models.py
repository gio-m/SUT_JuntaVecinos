from django.db import models
from django.forms import PasswordInput
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import pytz
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class TiposPerfil(models.Model):
    Tipo_Perfil_ID = models.AutoField(primary_key=True)
    Nombre_Perfil = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Nombre_Perfil
    
class JuntaVecinos(models.Model):
    Junta_Vecinos_ID = models.AutoField(primary_key=True)
    Nombre_Administrador = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=50)
    Localidad = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Administrador


class Vecinos(models.Model):
    rut = models.CharField(primary_key=True,max_length=15,verbose_name="Rut")
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    apellido = models.CharField(max_length=100,verbose_name="Apellido")
    direccion = models.CharField(max_length=100,verbose_name="Dirección")
    correo = models.EmailField(max_length=100,verbose_name="Correo")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    password = models.CharField(PasswordInput,max_length=100)
    certificado = models.ImageField(upload_to='images/certificados/',verbose_name="Certificado de residencia")
    
    

    
    def __str__(self):
        fila = "Rut: " + self.rut + '-' +"Nombre: " + self.nombre + '-' +"Apellido: " + self.apellido + '-' +"Dirección: " + self.direccion + '-' +"Correo: " + self.correo + '-' +"Fecha de nacimiento: " + self.fecha_nacimiento + '-' +"Contraseña: " + self.password
        
        return fila
    def delete(self, using=None,keep_parents=False):
        self.certificado.storage.delete(self.certificado.name)
        super().delete();


class Certificados(models.Model):
    ID = models.AutoField(primary_key=True)
    Vecino_RUT = models.ForeignKey(Vecinos, on_delete=models.CASCADE)
    FechaSolicitud = models.DateField()
    Aprobado = models.BooleanField()

    def __str__(self):
        return f"Certificado para {self.Vecino_RUT.Nombre} {self.Vecino_RUT.Apellido}"
    
    
##Formato de base de datos para las noticias
class Noticias(models.Model):
    opciones_noticias =[
                        ['Seguridad', 'Seguridad'],
                        ['Programas educativos', 'Programas educativos'],
                        ['Eventos', 'Eventos'],
                        ['Mejoras de infraestructura', 'Mejoras de infraestructura'],
                        ['Comités de vecinos', 'Comités de vecinos'],
                        ['Otros', 'Otros'] 
                    ] 
    id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100,verbose_name="Titulo")
    Tipo = models.CharField(max_length=100,choices=opciones_noticias, verbose_name="Tipo de noticia")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Fecha = models.DateField(verbose_name="Fecha de publicación")
    Imagen = models.ImageField(upload_to='images/noticias/', verbose_name="Imagen")

    def __str__(self):
        fila = "Titulo: " + self.Titulo + '-' +"Descripcion : " + self.Descripcion + '-' +"Tipo de noticia: " + self.get_Tipo_display() + '-' +"Fecha de publicacion: " + self.Fecha 
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete();


##Formato de base de datos para las proyectos
class Proyectos(models.Model):
    opciones_proyectos =[
                        ['Seguridad', 'Seguridad'],
                        ['Programas educativos', 'Programas educativos'],
                        ['Eventos', 'Eventos'],
                        ['Mejoras de infraestructura', 'Mejoras de infraestructura'],
                        ['Comités de vecinos', 'Comités de vecinos'],
                        ['Otros', 'Otros'] 
                    ] 
    id = models.AutoField(primary_key=True)
    TipoProyecto = models.CharField(max_length=100,choices=opciones_proyectos,verbose_name="Tipo de proyecto")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/proyectos/', verbose_name="Imagen")

    def __str__(self):
        fila = "Tipo de proyecto: " + self.get_TipoProyecto_display() + '-' +"Descripcion : " + self.Descripcion
        return f"{fila}"
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

##Formato de base de datos para las actividades
class Actividades(models.Model):
    opciones_actividades =[
                        ['Eventos', 'Eventos'],
                        ['Programas educativos', 'Programas educativos'],
                        ['Deportes', 'Deportes'],
                        ['Concursos', 'Concursos'],
                        ['Comités de vecinos', 'Comités de vecinos'],
                        ['Otros', 'Otros'] 
                    ] 
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,choices=opciones_actividades, verbose_name="Tipo de Actividad")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/actividades/', verbose_name="Imagen")
    fecha_actividad = models.DateField(verbose_name="Fecha de actividad")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.get_TipoSolicitud_display() + '-' +"Descripcion : " + self.Descripcion
        return f"{fila}"
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()


##Formato de base de datos para las propuestas
class Propuesta(models.Model):
    opciones_proyectos =[
                        ['Seguridad', 'Seguridad'],
                        ['Mejora de calles', 'Mejora de calles'],
                        ['Eventos', 'Eventos'],
                        ['Mejoras de infraestructura', 'Mejoras de infraestructura'],
                        ['Concursos', 'Concursos'],
                        ['Otros', 'Otros'] 
                    ] 
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,choices=opciones_proyectos, verbose_name="Tipo de propuesta")
    Descripcion = models.TextField(verbose_name="Descripcion")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.get_TipoSolicitud_display() + '-' +"Descripcion : " + self.Descripcion
        return f"{fila}"
    def delete(self, using=None,keep_parents=False):
        super().delete()
#CLAUDIO
##Formato de base de datos para los documentos   



class Documentos (models.Model):
    nombre_documento = models.CharField(max_length=100, verbose_name="Nombre del Documento")
    

    TIPO_DOCUMENTO_CHOICES = [
        ("Certificado de residencia", "Certificado de residencia"),
        ("Boleta", "Boleta"),
    ]

    tipo_documento = models.CharField(
        max_length=50,
        choices=TIPO_DOCUMENTO_CHOICES,
        verbose_name="Tipo de Documento"
    )

    fecha_publicacion = models.DateTimeField(
        verbose_name="Fecha de Publicación",
        editable=False,  
        )
    
   
    
    descripcion_documento = models.TextField(verbose_name="Descripción del Documento")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Agrega algún documento o boleta que compruebe tu identidad")
    
    def save(self, *args, **kwargs):
        if not self.fecha_publicacion:
            self.fecha_publicacion = timezone.now().astimezone(pytz.timezone("Chile/Continental"))
        super(Documentos, self).save(*args, **kwargs)
        
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.fecha_publicacion:
            self.fecha_publicacion = timezone.now().astimezone(pytz.timezone("Chile/Continental"))
        super(Documentos, self).save(*args, **kwargs)

    def __str__(self):
        return f"Documento: {self.nombre_documento} ({self.get_tipo_documento_display()})"
    
class Notificaciones(models.Model):
    Notificaciones_id = models.AutoField(primary_key=True)
    Titulo_notificaciones = models.CharField(max_length=100)
    Contenido = models.CharField(max_length=100)
    FechaEnvio = models.DateTimeField()
    Tipo_notificaciones = models.CharField(max_length=20)
    Destinatario = models.ForeignKey('Vecinos', on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo_notificaciones