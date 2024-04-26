from django.contrib import admin

from .models import ImagenCarrusel


# Register your models here.
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'created', 'visible']
    search_fields = ['created', 'visible']

