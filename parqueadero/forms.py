from django import forms
from .models import Programa
#from django.core.validators import RegexValidator

# password_validator = RegexValidator(
#     regex=r'^[0-9ABCD*#]+$',
#     message="La contraseña debe contener solo números del 0 al 9, las letras A, B, C, D, y los caracteres '*' y '#'."
# )

class usuariosForm(forms.Form):

    nombre = forms.CharField(label="Nombre",max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Carlos Andres'}), required=True)
    apellido = forms.CharField(label="apellido",max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Burgos Aristizabal'}), required=True)
    codigo = forms.CharField(label="codigo",max_length=11,widget=forms.TextInput(attrs={'placeholder': 'maximo 11 digitos'}), required=True)
    identificacion = forms.CharField(label="identificacion",max_length=11,widget=forms.TextInput(attrs={'placeholder': 'CC,TI'}), required=True)
    email = forms.EmailField(label="email",max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ejemplo:carlos@gmailcom'}), required=True)
    password =forms.CharField(label="contraseña",max_length=250, required=True, widget=forms.PasswordInput)
    #password =forms.CharField(label="contraseña",max_length=250,validators=[password_validator], required=True, widget=forms.PasswordInput)
    
    id_programa = forms.ModelChoiceField(label="programa", queryset= Programa.objects.all(), empty_label='Seleccione el programa') 

class inicioForm(forms.Form):
    email = forms.CharField(label="email",max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Ejemplo:carlos@gmailcom'}), required=True)
    password =forms.CharField(label="contraseña",max_length=250, required=True,widget=forms.PasswordInput)
    
    