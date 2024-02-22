"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Edu CRM API",
      default_version='v1',
      description="Docs for lms api",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/accounts/', include('apps.accounts.urls')),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("sohib/", include('api.sohib.urls')),
    path("qudrat/", include('api.qudrat.urls')),
    path("abbos/", include('api.abbos.urls')),
    path("abdulaziz/", include('api.abdulaziz.urls')),
    path("aligarx/", include('api.aligarx.urls')),
    path("bekzod/", include('api.bekzod.urls')),
    path("javlonbek/", include('api.javlonbek.urls')),
    path("mehroj/", include('api.mehroj.urls')),
    path("samandar/", include('api.samandar.urls')),
    path("sardor/", include('api.sardor.urls')),
    path("shahlo/", include('api.shahlo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)