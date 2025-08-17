from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import FrontendAppView  

urlpatterns = [
    path('admin/api/', include('caja.urls')),
    path('admin/', admin.site.urls),
    path('socios/', include('socios.urls')), 
    path('clases/', include('clases.urls')), 
]

urlpatterns += [
    re_path(r'^.*$', FrontendAppView.as_view(), name="frontend"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)