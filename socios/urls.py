# urls.py

from django.urls import path
from .views import PerfilSocio

urlpatterns = [
    path('perfil/', PerfilSocio.as_view(), name='perfil'),

]
