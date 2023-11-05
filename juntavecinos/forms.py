from django import forms 
from .models import Noticias, Actividades, Proyectos, Propuesta, Vecinos, Documentos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
class FormularioDocumentos(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['nombre_documento', 'tipo_documento', 'fecha_publicacion', 'descripcion_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(FormularioDocumentos, self).__init__(*args, **kwargs)
        
        
class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email
	