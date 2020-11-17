from django import forms
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
    class Meta:
        models = Autor
        fiels = ['nombre','apellidos','nacionalidad','descripcion']

class Form(forms.ModelForm):
    
    class Meta:
        models = Libro 
        fields = ("titulo",'fecha_publicacion','autor_id',)

