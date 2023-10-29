from django.urls import include, path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('nosotros', views.nosotros, name='nosotros'),
    path('juntas/crear', views.crear, name='crear'),
    path('index', views.index, name='index'),
    path('form', views.form, name='form'),
    path('juntas/editarnoticia', views.editarnoticia, name='editarnoticia'),
    path('juntas/iniciojunta', views.iniciojunta, name='iniciojuntas'),
    path('juntas/actividades', views.actividades, name='actividades'),
    path('eliminarnoticia/<int:id>', views.eliminarnoticia, name='eliminarnoticia'),
    path('juntas/editarnoticia/<int:id>', views.editarnoticia, name='editarnoticia'),

    path('juntas/revisaractividad', views.revisaractividad, name='revisaractividad'),
    path('eliminaractividad/<int:id>', views.eliminaractividad, name='eliminaractividad'),
    path('juntas/editaractividad/<int:id>', views.editaractividad, name='editaractividad'),

    path('juntas/revisarproyecto', views.revisarproyecto, name='revisarproyecto'),
    path('juntas/proyectos', views.proyectos, name='proyectos'),
    path('juntas/editarproyecto/<int:id>', views.editarproyecto, name='editarproyecto'),
    path('eliminarproyecto/<int:id>', views.eliminarproyecto, name='eliminarproyecto'),
    
    #CLAUDIO
    path('solicitud_documentos', views.solicitud_documentos, name='solicitud_documentos'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                 