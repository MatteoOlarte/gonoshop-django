from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import ImagenCarrusel


# Create your views here.
def pagina_inicio(request: HttpRequest) -> HttpResponse:
    carrusel_img = ImagenCarrusel.objects.filter(visible=True)

    context = {
        'nombre_url': '',
        'carrusel': carrusel_img
    }
    return render(request, 'pagina_inicio/index/index-template.html', context)


def pagina_inicio_redirects(request: HttpRequest) -> HttpResponse:
    return redirect('home:index')
