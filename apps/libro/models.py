from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,blank=False,null=False)
    apellidos = models.CharField(max_length=100,blank=False,null=False)
    nacionalidad = models.CharField(max_length=200,blank=False,null=False)
    descripcion = models.TextField(blank=False,null=False)
    fecha_registro = models.DateField("Fecha de registro", auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=100,blank=False,null=False)
    fecha_publicacion = models.DateField('Fecha de publicación',blank=False,null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_registro = models.DateField('Fecha de registro',auto_now=True,auto_now_add=False)
    
    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo