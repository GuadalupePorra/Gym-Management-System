from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioSViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioSViewSet)

urlpatterns = [
    path('', include(router.urls)),
]