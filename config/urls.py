from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Project Base",
        default_version=1,
        description="An API App Project Base",
        contact=openapi.Contact(email="zeyadslama23@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [ 
    path("api/v1/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core_apps.accounts.urls")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
]


admin.site.site_header = "Project Base"  # Sets the header in the admin
# Sets the title on the browser tab
admin.site.site_title = "Project Base"
# Sets the index page title
admin.site.index_title = "Welcome to Project Base"


# Serve static and media files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
