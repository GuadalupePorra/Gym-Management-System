from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import FrontendAppView  

urlpatterns = [
    path('admin/api/', include('caja.urls')),
    path('admin/', admin.site.urls),
    path('socios/', include('socios.urls')), 
    path('clases/', include('clases.urls')), 
]

# Sirve archivos en /media/ en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Sirve archivos en /static/ en desarrollo
urlpatterns += staticfiles_urlpatterns()

# Ruta final: React SPA (debe ir al final para no interceptar otras rutas)
urlpatterns += [
    re_path(r'^.*$', FrontendAppView.as_view(), name="frontend"),
]
