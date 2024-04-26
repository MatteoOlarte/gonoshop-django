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
    