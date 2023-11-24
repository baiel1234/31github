from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("world/", include("world.urls")),
    path("admin/", admin.site.urls),
]