from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("go/", include("shorts.urls")),
    path("api/", include("server.api.urls")),
    path("accounts/", include("allauth.urls")),
    path('admin/docs/', include("django.contrib.admindocs.urls")),
    path('admin/', admin.site.urls),
]
