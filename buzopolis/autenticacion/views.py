from django.shortcuts import render
from django.http import HttpRequest, HttpResponse   


# Create your views here.
def vista_registro(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Registro')


def vista_login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login')