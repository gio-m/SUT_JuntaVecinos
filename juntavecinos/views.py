from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView
from django.http import HttpResponse
from .models import Vecinos,Noticias,Propuesta,Proyectos,Actividades,Documentos
from .forms import NoticiasForm, ActividadesForm, ProyectosForm, PropuestaForm, VecinosForm, FormularioDocumentos
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def inicio(request):    
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def crear(request):
    formularionoticia = NoticiasForm(request.POST or None, request.FILES or None)
    if formularionoticia.is_valid():
        formularionoticia.save()
        return redirect('crear')
    return render(request, 'juntas/crear.html', {'formularionoticia':formularionoticia})


def index(request):
    noticias = Noticias.objects.all().order_by('id')
    print (Noticias)
    return render(request, 'juntas/index.html', {'noticias':noticias})


def form(request):
    return render(request, 'juntas/form.html')
def formularioactividad(request):
    return render(request, 'juntas/formularioactividad.html')
def formularioproyecto(request):
    return render(request, 'juntas/formularioproyecto.html')

def proyectos(request):
    formularioproyecto = ProyectosForm(request.POST or None, request.FILES or None)
    if formularioproyecto.is_valid():
        formularioproyecto.save()
        return redirect('proyectos')
    return render(request, 'juntas/proyectos.html', {'formularioproyecto':formularioproyecto})


def actividades(request):
    formularioactividad = ActividadesForm(request.POST or None, request.FILES or None)
    if formularioactividad.is_valid():
        formularioactividad.save()
        return redirect('actividades')
    return render(request, 'juntas/actividades.html', {'formularioactividad':formularioactividad})

def revisaractividad(request):
    actividades = Actividades.objects.all().order_by('id')
    print (actividades)
    return render(request, 'juntas/revisaractividad.html', {'actividades':actividades})

def revisarproyecto(request):
    proyectos = Proyectos.objects.all().order_by('id')
    print (proyectos)
    return render(request, 'juntas/revisarproyecto.html', {'proyectos':proyectos})


def iniciojunta(request):    
    return render(request, 'juntas/iniciojunta.html')   

def eliminarnoticia(request,id):
    noticias = Noticias.objects.get(id=id)
    noticias.delete()
    return redirect('crear')

def editarnoticia(request,id):
    noticias = Noticias.objects.get(id=id)
    formularionoticia = NoticiasForm(request.POST or None, request.FILES or None, instance=noticias)
    if formularionoticia.is_valid() and request.POST:
        formularionoticia.save()
        return redirect('crear') 
    return render(request,'juntas/editarnoticia.html',{'formularionoticia':formularionoticia})

def eliminaractividad(request,id):
    actividades = Actividades.objects.get(id=id)
    actividades.delete()
    return redirect('actividades')

def editaractividad(request,id):
    actividades = Actividades.objects.get(id=id)
    formularioactividad = ActividadesForm(request.POST or None, request.FILES or None, instance=actividades)
    if formularioactividad.is_valid() and request.POST:
        formularioactividad.save()
        return redirect('actividades') 
    return render(request,'juntas/editaractividad.html',{'formularioactividad':formularioactividad})

def editarproyecto(request,id):
    proyectos = Proyectos.objects.get(id=id)
    formularioproyecto = ProyectosForm(request.POST or None, request.FILES or None, instance=proyectos)
    if formularioproyecto.is_valid() and request.POST:
        formularioproyecto.save()
        return redirect('proyectos') 
    return render(request,'juntas/editarproyecto.html',{'formularioproyecto':formularioproyecto})

def eliminarproyecto(request,id):
    proyectos = Proyectos.objects.get(id=id)
    proyectos.delete()
    return redirect('proyectos')

#CLAUDIO

def solicitud_documentos(request):
    if request.method == 'POST':
        formulariodocumentos = FormularioDocumentos(request.POST, request.FILES)
        if formulariodocumentos.is_valid():
        
            formulariodocumentos.save()

          
            return redirect('solicitud_documentos')

    else:
        formulariodocumentos = FormularioDocumentos()

    context = {
        'formulariodocumentos': formulariodocumentos,
    }

    return render(request, 'juntas/solicitud_documentos.html', context)


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)