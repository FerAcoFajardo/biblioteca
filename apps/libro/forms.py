from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']

"""class Form(forms.ModelForm):
    
    class Meta:
        models = Libro 
        fields = ("titulo",'fecha_publicacion','autor_id',)

"""