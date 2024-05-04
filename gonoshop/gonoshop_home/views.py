from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import ImagenCarrusel


# Create your views here.
def pagina_inicio(request: HttpRequest) -> HttpResponse:
    carrusel = ImagenCarrusel.objects.filter(visible=True)
    context = {
        'nombre_url': 'home:index',
        'carrusel': carrusel,
    }
    return render(request, 'gonoshop_home/index/template.html', context)


def redirect_to_inicio(_: HttpRequest) -> HttpResponse:
    return redirect('home:index')