from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def pagina_inicio(request: HttpRequest) -> HttpResponse:
    return render(request, 'pagina_inicio/index/index-template.html')


def pagina_inicio_redirects(request: HttpRequest) -> HttpResponse:
    return redirect('home:index')
