from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import ImagenCarrusel
from .models import ItemPortafolio

# Create your views here.
def pagina_inicio(request: HttpRequest) -> HttpResponse:
    carrusel = ImagenCarrusel.objects.filter(visible=True)
    portafolio = ItemPortafolio.objects.filter(visible=True)
    context = {
        'nombre_url': 'home:index',
        'carrusel': carrusel,
        'portafolio': portafolio
    }
    return render(request, 'pagina_inicio/index/index-template.html', context)


def pagina_inicio_redirects(_: HttpRequest) -> HttpResponse:
    return redirect('home:index')
