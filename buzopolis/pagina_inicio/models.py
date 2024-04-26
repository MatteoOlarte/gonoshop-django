from django.db import models


# Create your models here.
class ImagenCarrusel(models.Model):
    class Meta:
        verbose_name = 'Imagen Carrusel'
        verbose_name_plural = 'Imágenes Carrusel'

    
    titulo = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    imagen = models.ImageField(upload_to='home/carrusel')
    created = models.DateField(auto_now_add=True) 
    visible = models.BooleanField(default=False)
    

class ItemPortafolio(models.Model):
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Item del Portafolio'
        verbose_name_plural = 'Items del Portafolio'
        

    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    sub_titulo = models.CharField(max_length=50, verbose_name='Sub Titulo')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    imagen = models.ImageField(upload_to='home/portafolio')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=False, verbose_name='Mostrar en la Pagina Web')