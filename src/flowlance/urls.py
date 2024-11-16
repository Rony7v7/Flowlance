"""
URL configuration for flowlance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("user.urls")),  # Incluye las URLs de acceso de usuarios
    path('profile/', include('profile.urls')),  # Incluye URLs de perfiles
    path("project/", include("project.urls")),  # Incluye URLs de control de proyectos
    path('dashboard/', include('dashboard.urls')),  # Incluye URLs del dashboard
    path('chat/',include('chat.urls')),  # Incluye las URLs de chat
    path('notifications/', include('notifications.urls')),  # Incluye las URLs de notificaciones
    path('payment/', include('payment.urls')),  # Incluye las URLs de pagos
    path('settings/', include('settings.urls')),  # Incluye las URLs de configuración
    path("accounts/", include("allauth.urls")),  # Incluye las URLs de autenticación social
    path("i18n/", include("django.conf.urls.i18n")), #Url encargada de todas las 
]

# Add static and media files in debug modej
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
