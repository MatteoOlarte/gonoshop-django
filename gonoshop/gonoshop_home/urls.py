from django.urls import path

from .views import pagina_inicio
from .views import redirect_to_inicio


urlpatterns = [
    path('home/', pagina_inicio, name='index'),
    path('', redirect_to_inicio)
]
