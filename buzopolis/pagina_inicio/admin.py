from django.contrib import admin

from .models import ImagenCarrusel
from .models import ItemPortafolio


# Register your models here.
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'created', 'visible']
    search_fields = ['titulo']
    list_filter = ['created', 'visible']


@admin.register(ItemPortafolio)
class ItemPortafolioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'created', 'visible']
    search_fields = ['titulo', 'sub_titulo']
    list_filter = ['visible', 'created']
