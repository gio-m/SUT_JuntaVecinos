from django import forms 
from .models import Noticias, Actividades, Proyectos, Propuesta, Vecinos, Documentos

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__'



class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividades
        fields = '__all__'



class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'



class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = '__all__'



class VecinosForm(forms.ModelForm):
    class Meta:
        model = Vecinos
        fields = '__all__'
        
#CLAUDIO
class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['NombreDocumento', 'DescripcionDocumento', 'Archivo']