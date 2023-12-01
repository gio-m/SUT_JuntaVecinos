import pytz
from django import forms 
from .models import Noticias, Actividades, Proyectos, Propuesta, Vecinos, Documentos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
def validate_file_size(value):
    filesize = value.size
    if filesize > 20 * 1024 * 1024:  
        raise ValidationError(_('El archivo no puede superar los 20 MB.'))

class FormularioDocumentos(forms.ModelForm):
    TIPO_DOCUMENTO_CHOICES = [
        ("", "Seleccionar tipo de documento --"),  
        ("Certificado de residencia", "Certificado de residencia"),
        ("Boleta", "Boleta"),
    ]

    tipo_documento = forms.ChoiceField(
        choices=TIPO_DOCUMENTO_CHOICES,
        label="Tipo de Documento",
        required=True,
    )

    archivo = forms.FileField(
        label="Agrega algún documento o boleta que compruebe tu identidad",
        required=True,
        help_text="Se permite un tamaño máximo de 20 MB.",
        validators=[validate_file_size] 
    )

    class Meta:
        model = Documentos
        fields = ['nombre_documento', 'tipo_documento', 'descripcion_documento', 'archivo']

    def __init__(self, *args, **kwargs):
        super(FormularioDocumentos, self).__init__(*args, **kwargs)

    def clean_tipo_documento(self):
        tipo_documento = self.cleaned_data.get('tipo_documento')
        if tipo_documento == "":
            raise forms.ValidationError("Debes seleccionar un tipo de documento")
        return tipo_documento
    
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
	