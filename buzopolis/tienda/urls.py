from django.contrib import admin
from django.urls import path

from .views import pagina_inicio
from .views import pagina_inicio_redirect
from .views import lista_productos
from .views import detalle_producto


urlpatterns = [
    path("", pagina_inicio_redirect),
    path("home", pagina_inicio, name='inicio'),
    path("tienda", lista_productos, name='lista_productos'),
    path("tienda/producto", detalle_producto, name='detalle_producto')
]
