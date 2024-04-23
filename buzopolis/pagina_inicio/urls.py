from django.contrib import admin
from django.urls import path, include

from .views import pagina_inicio
from .views import pagina_inicio_redirects


urlpatterns = [
    path("home", pagina_inicio, name='index'),
    path("", pagina_inicio_redirects)
]
