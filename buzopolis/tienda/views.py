from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def pagina_inicio(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Pagina De Inicio')


def pagina_inicio_redirect(request: HttpRequest) -> HttpResponse:
    return redirect('tienda:inicio')


def lista_productos(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Compra de productos')


def detalle_producto(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Detalle Del Producto')