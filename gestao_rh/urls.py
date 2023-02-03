from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('hora-extra/', include('apps.registro_hora_extra.urls')),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)