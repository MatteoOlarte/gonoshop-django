from django.db import models
from typing import override
from django.db import models
from django.urls import reverse

from gonoshop_auth.models import User

# Create your models here.
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre Categoría')

    @override
    def __str__(self) -> str:
        return self.nombre


class ColorProducto(models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre Color')

    @override
    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        indexes = [
            models.Index(fields=['slug'], name='idx_producto_slug'),
            models.Index(fields=['-precio'], name='idx_producto_precio')
        ]
        ordering = ['-precio']

    class Tallas(models.TextChoices):
        XS = ('xs', 'extra small')
        S = ('s', 'small')
        M = ('m', 'medium')
        L = ('l', 'large')
        XL = ('xl', 'extra large')
        XXL = ('xxl', 'extra extra large')

    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=2500)
    imagen = models.ImageField(upload_to='tienda/productos/%Y/%m/%d/%H')
    talla = models.CharField(max_length=3, choices=Tallas.choices, default=Tallas.S)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()
    disponibilidad = models.BooleanField(default=True, editable=False)
    publicado = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    color = models.ManyToManyField(
        to=ColorProducto,
        related_name="+",
        related_query_name="+"
    )
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
        self.disponibilidad = (self.stock != 0)
        super(Producto, self).save(args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('tienda:detalle_producto', args=[self.slug, self.id])
    

    def get_price_format(self) -> str:
        return f'${self.precio:,.2f}'


class Personalizado(models.Model):
    nombre = models.CharField(max_length=250)
    # aquí deben poner atributos como posición de la imagen, la imagen
    # y el producto al cual apunta este diseño


class ComentarioProducto(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.CharField(max_length=25000)
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

    

