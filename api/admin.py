from django.urls import path
from . import views  # Asegúrate de que views.py esté en la misma carpeta

urlpatterns = [
    path('', views.your_view_function, name='api'),  # Cambia 'your_view_function' por el nombre de tu vista
]