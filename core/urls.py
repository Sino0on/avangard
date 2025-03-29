from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/v1/objects/", include("objects.urls")),
    path("api/v1/news/", include("news.urls")),
    path("api/v1/contact/", include("info.urls")),
    path("api/v1/home/", include("home.urls")),
    path("api/v1/about/", include("about.urls")),
    path("api/v1/tender/", include("tender.urls")),
    path('admin/', admin.site.urls),
    # path("i18n/", include("django.conf.urls.i18n")),
    path("api/v1/docs/", include("openapi.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
