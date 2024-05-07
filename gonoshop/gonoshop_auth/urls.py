from django.urls import path

from .views import login_view
from .views import register_view


urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
] 
