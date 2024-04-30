from typing import override
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=250)


class Producto(models.Model):
    class Tallas(models.TextChoices):
        XS = ('xs', 'extra small')
        S = ('s', 'small')
        M = ('m', 'medium')
        L = ('l', 'large')
        XL = ('xl', 'extra large')
        XXL = ('xxl', 'extra extra large')

    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    precio = models.DecimalField()
    description = models.TextField(max_length=2500)
    talla = models.CharField(max_length=2, choices=Tallas, default=Tallas.S)
    color = models.CharField(max_length=250)
    stock = models.IntegerField()
    disponibilidad = models.BooleanField(default=True, editable=False)
    publicado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='tienda/productos/%Y/%m/%d/%H')
    tipo_producto = models.ForeignKey(
        to=TipoProducto,
        on_delete=models.RESTRICT,
        related_name='productos',
        related_query_name='producto'
    )

    @override
    def save(self, *args, **kwargs) -> None:
        '''
        Sobrescribe el método save para actualizar la disponibilidad del producto.

        Si el stock es 0, la disponibilidad se establece en False. De lo contrario,
        se establece en True.
        '''
        self.disponibilidad = (self.stock == 0)
        super(Producto, self).save(args, **kwargs)


class Personalizado(models.Model):
    nombre = models.CharField(max_length=250)
    # aquí deben poner atributos como posición de la imagen, la imagen
    # y el producto al cual apunta este diseño


class ComentarioProducto(models.Model):
    titulo = models.CharField(250)
    contenido = models.CharField(25000)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comentarios',
        related_query_name='comentario'
    )
    producto = models.ForeignKey(
        to=Producto,
        on_delete=models.CASCADE,
        related_name='comentarios',
        related_query_name='comentario'
    )
