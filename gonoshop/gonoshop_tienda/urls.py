from django.urls import path

from .views import lista_productos_all
from .views import detalle_producto
from .views import editor_producto


urlpatterns = [
    path('', lista_productos_all, name='lista_productos'),
    path('<slug:nombre_producto>/<int:_id>', detalle_producto, name='detalle_producto'),
    path('designer/', editor_producto, name='editor_producto')
]