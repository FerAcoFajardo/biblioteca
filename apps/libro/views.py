from django.shortcuts import render,redirect
from .forms import AutorForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def Home(request):
    return render(request,'index.html')

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('home')
    else:
        autor_form = AutorForm()
        print(autor_form)

    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.all()
    return render(request,'libro/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST,instance=autor)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('home')
    except ObjectDoesNotExist as e:
        error = e
    
        return render(request,'libro/crear_autor.html',{'error':error})