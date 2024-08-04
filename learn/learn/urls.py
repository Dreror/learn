from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("new.urls")),
    path("new_2/", include("new_2.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
