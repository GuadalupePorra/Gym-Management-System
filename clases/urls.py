from django.urls import path
from .views import *

urlpatterns = [
    path('inscribirse/', InscribirseClase.as_view(), name='inscribirse_clase'),
    path('darse_baja/', DarseBajaClase.as_view(), name='darse_baja_clase'),

]

