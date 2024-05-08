from django.urls import path

from .views import pago_producto


urlpatterns = [
    path('<int:id>', pago_producto, name='pago_producto')
]