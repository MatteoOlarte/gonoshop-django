from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def lista_productos_all(request: HttpRequest) -> HttpResponse:
    context = {
        'url_name': 'tienda'
    }
    return render(request, 'tienda_buzopolis/lista_productos/template_all.html', context)


def lista_productos_filter(request: HttpRequest, category: str) -> HttpResponse:
    context = {
        'url_name': 'tienda',
        'category': category
    }
    return render(request, 'tienda_buzopolis/lista_productos/template_filter.html', context)


def detalle_producto(request: HttpRequest, nombre_producto: str, _id: int) -> HttpResponse:
    context = {
        'url_name': 'tienda'
    }
    return render(request, 'tienda_buzopolis/detalle_producto/template.html', context)


def editor_producto(request: HttpRequest, nombre_producto: str, _id: int) -> HttpResponse:
    context = {
        'url_name': 'tienda'
    }
    return render(request, 'tienda_buzopolis/editor_producto/template.html', context)
