from django.contrib import admin

from .models import ColorProducto
from .models import Producto
from .models import TipoProducto


# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_producto', 'color', 'talla', 'precio', 'stock', 'disponibilidad', 'publicado']
    list_filter = ['tipo_producto', 'color', 'talla', 'precio', 'disponibilidad', 'stock', 'publicado']
    search_fields = ['nombre', 'tipo_producto__nombre', 'color__nombre', 'description']
    date_hierarchy = 'created'
    raw_id_fields = ['color', 'tipo_producto']
    prepopulated_fields = {'slug': ['nombre']}


@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(ColorProducto)
class ColorProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']