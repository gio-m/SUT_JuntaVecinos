from django.db import models
from django.forms import PasswordInput

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
    id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100,verbose_name="Titulo")
    Tipo = models.CharField(max_length=100,verbose_name="Tipo de noticia")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Fecha = models.DateField(verbose_name="Fecha de publicación")
    Imagen = models.ImageField(upload_to='images/noticias/', verbose_name="Imagen")

    def __str__(self):
        fila = "Titulo: " + self.Titulo + '-' +"Descripcion : " + self.Descripcion + '-' +"Tipo de noticia: " + self.Tipo + '-' +"Fecha de publicacion: " + self.Fecha 
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete();


##Formato de base de datos para las proyectos
class Proyectos(models.Model):
    id = models.AutoField(primary_key=True)
    TipoProyecto = models.CharField(max_length=100,verbose_name="Tipo de proyecto")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/proyectos/', verbose_name="Imagen")

    def __str__(self):
        fila = "Tipo de proyecto: " + self.TipoProyecto + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

##Formato de base de datos para las actividades
class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,verbose_name="Tipo de solicitud")
    Descripcion = models.TextField(verbose_name="Descripcion")
    Imagen = models.ImageField(upload_to='images/actividades/', verbose_name="Imagen")
    fecha_actividad = models.DateField(verbose_name="Fecha de actividad")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.TipoSolicitud + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()


##Formato de base de datos para las propuestas
class Propuesta(models.Model):
    id = models.AutoField(primary_key=True)
    TipoSolicitud = models.CharField(max_length=100,verbose_name="Tipo de solicitud")
    Descripcion = models.TextField(verbose_name="Descripcion")
    def __str__(self):
        fila = "Tipo de solicitud: " + self.TipoSolicitud + '-' +"Descripcion : " + self.Descripcion
        return fila
    def delete(self, using=None,keep_parents=False):
        super().delete()

#CLAUDIO
##Formato de base de datos para los documentos   

class Documentos(models.Model):
    id = models.AutoField(primary_key=True)
    NombreDocumento = models.CharField(max_length=100, verbose_name="Nombre del Documento")
    TipoDocumento = models.CharField(max_length=50, verbose_name="Tipo de Documento")
    FechaPublicacion = models.DateField(verbose_name="Fecha de Publicación")
    DescripcionDocumento = models.TextField(verbose_name="Descripción del Documento")
    Archivo = models.FileField(upload_to='documents/', verbose_name="Archivo del Documento")

    def __str__(self):
        return f"Documento: {self.NombreDocumento} ({self.TipoDocumento})"

    def delete(self, using=None, keep_parents=False):
        self.Archivo.storage.delete(self.Archivo.name)
        super().delete()

class Reuniones(models.Model):
    Reuniones_id = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Lugar = models.CharField(max_length=100)
    Asunto = models.CharField(max_length=100)
    Descripcion_reuniones = models.TextField(max_length=500)
    Proyecto_id = models.ForeignKey(Proyectos, on_delete=models.CASCADE)

    def __str__(self):
        return self.Asunto
    

class Notificaciones(models.Model):
    Notificaciones_id = models.AutoField(primary_key=True)
    Titulo_notificaciones = models.CharField(max_length=100)
    Contenido = models.CharField(max_length=100)
    FechaEnvio = models.DateTimeField()
    Tipo_notificaciones = models.CharField(max_length=20)
    Destinatario = models.ForeignKey('Vecinos', on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo_notificaciones