from django.urls import path
from .views import *

urlpatterns = [
    path('crear_autor/',crearAutor,name='crear_autor'),
    path('listar_autor/',listarAutor,name='listar_autor'),
    path('editar_autor/usuario:<int:id>',editarAutor,name='editar_autor'),
    path('eliminar_autor/usuario:<int:id>',eliminarAutor,name='eliminar_autor')

    

]


