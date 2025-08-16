from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/api/', include('caja.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('socios/', include('socios.urls')), 
    path('clases/', include('clases.urls')), 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^.*$', FrontendAppView.as_view(), name="frontend"),
]
